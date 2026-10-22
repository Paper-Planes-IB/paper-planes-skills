#!/usr/bin/env node
/* Optional Playwright collector. No forms, clicks, logins or website edits. */
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const dns = require('node:dns').promises;
const {spawnSync} = require('node:child_process');

function argsOf(argv) {
  const a = {widths: '360,412,1365', repeats: 3, window: 5000, timeout: 20000, maxRequests: 200, maxPages: 3, maxResources:200, maxTransferBytes:20*1024*1024, maxDomElements:15000, maxLinks:1000, coverageMaxBytes:2*1024*1024, coverage:false};
  for (let i=0; i<argv.length; i++) {
    if (!argv[i].startsWith('--')) throw Error('Нужны именованные аргументы');
    const k = argv[i].slice(2);
    if (k === 'allow-local') {a.allowLocal = true; continue;}
    if (i+1 === argv.length) throw Error('Нет значения: '+k);
    a[k] = argv[++i];
  }
  if (!a.audit) throw Error('Нужен --audit <каталог HTTP-аудита>');
  a.outputName=a['output-name'] || 'browser.json';
  if(!/^browser(?:\.[a-z0-9-]+)?\.json$/.test(a.outputName))throw Error('--output-name: только browser.json или browser.<метка>.json');
  a.repeats = Number(a.repeats); a.window = Number(a.window); a.timeout = Number(a.timeout);
  a.maxRequests = Number(a['max-requests'] ?? a.maxRequests); a.maxPages = Number(a['max-pages'] ?? a.maxPages);
  for (const [key,flag] of [['maxResources','max-resources'],['maxTransferBytes','max-transfer-bytes'],['maxDomElements','max-dom-elements'],['maxLinks','max-links'],['coverageMaxBytes','coverage-max-bytes']]) a[key]=Number(a[flag] ?? a[key]);
  if (a.coverage !== false && !['yes','no'].includes(a.coverage)) throw Error('--coverage принимает yes или no');
  a.coverage=a.coverage==='yes';
  if ([a.repeats,a.window,a.timeout,a.maxRequests,a.maxPages,a.maxResources,a.maxTransferBytes,a.maxDomElements,a.maxLinks,a.coverageMaxBytes].some(n=>!Number.isSafeInteger(n)) || a.timeout<1000 || a.timeout>120000 || a.maxRequests>2000 || a.maxResources<1 || a.maxResources>2000 || a.maxTransferBytes<1024 || a.maxTransferBytes>100*1024*1024 || a.maxDomElements<10 || a.maxDomElements>50000 || a.maxLinks<1 || a.maxLinks>5000 || a.coverageMaxBytes<1024 || a.coverageMaxBytes>10*1024*1024) throw Error('Некорректные границы ресурсов, DOM, покрытия или timeout');
  a.widths = a.widths.split(',').map(Number);
  if (a.repeats < 3 || a.repeats > 10 || a.window < 1000 || a.window > 30000 || a.maxPages < 1 || a.maxPages > 20 || a.maxRequests < 1 ||
      !a.widths.length || a.widths.length>10 || a.widths.some(w=>!Number.isSafeInteger(w) || w<320 || w>2560)) throw Error('Некорректные лимиты: repeats 3–10, window 1000–30000, pages 1–20, widths 320–2560');
  return a;
}

function publicIP(ip, allowLocal) {
  const py=spawnSync(process.env.AUDIT_PYTHON || 'python3',['-c',
    'import json,sys,ipaddress; d=json.load(sys.stdin); a=ipaddress.ip_address(d["ip"]); a=getattr(a,"ipv4_mapped",None) or a; print("yes" if a.is_global or (d["local"] and a.is_loopback) else "no")'],
    {input:JSON.stringify({ip,local:!!allowLocal}),encoding:'utf8'});
  return py.status===0 && py.stdout.trim()==='yes';
}

const normalized = s => {const u=new URL(s); u.hash=''; return u.href;};

// Scope decisions are frame-aware. A frame is a separate document, not the parent page.
function classifyRequest(req,page,site,manifest) {
  let frame; try {frame=req.frame();} catch {}
  const is_main_document=req.resourceType()==='document' && frame===page.mainFrame();
  let reason=null;
  try {
    const u=new URL(req.url());
    if (req.resourceType()==='document' && u.host!==site.host) reason='документ другого хоста вне охвата';
    else if (req.resourceType()==='document' && u.search && !manifest.config.include_query) reason='параметрический документ вне охвата';
  } catch {reason='некорректный адрес запроса';}
  return {is_main_document,reason,frame_url:frame?.url() || null};
}

function usedCoverageUnits(ranges,total) {
  // V8 nested zero-count ranges override an enclosing used range. Never sum them.
  const events=new Map(); let id=0;
  for(const r of ranges) {
    const start=Math.max(0,r.startOffset),end=Math.min(total,r.endOffset);
    if(end<=start) continue;
    const item={id:id++,start,end,count:r.count};
    if(!events.has(start))events.set(start,[]);if(!events.has(end))events.set(end,[]);
    events.get(start).push({add:item});events.get(end).push({remove:item.id});
  }
  const active=new Map();let used=0,previous=0;
  for(const pos of [...events.keys()].sort((a,b)=>a-b)) {
    let winner;
    for(const r of active.values())if(!winner || r.end-r.start<winner.end-winner.start || (r.end-r.start===winner.end-winner.start && r.id>winner.id))winner=r;
    if(winner?.count>0)used+=pos-previous;
    for(const ev of events.get(pos))if(ev.remove!==undefined)active.delete(ev.remove);else active.set(ev.add.id,ev.add);
    previous=pos;
  }
  return used;
}

async function networkProbe(ctx,page,a) {
  const output={supported:false,total_encoded_bytes:0,total_decoded_body_bytes:0,resource_count:0,resources:[],resources_truncated:false,byte_budget_exceeded:false,byte_limit:a.maxTransferBytes};
  let cdp,mainFrameId=null; const rows=new Map(),scripts=new Map(),styles=new Map(),executionContexts=new Map(); let transferred=0,stopping=false,coverageDiscoveryTruncated=false;
  try {
    cdp=await ctx.newCDPSession(page); await cdp.send('Network.enable');output.supported=true;
    cdp.on('Network.requestWillBeSent',e=>{
      output.resource_count++;
      if(rows.size>=a.maxResources){output.resources_truncated=true;return;}
      rows.set(e.requestId,{url:e.request.url,type:e.type,initiator_type:e.initiator?.type || null,status:null,encoded_bytes:0,decoded_body_bytes:0,finished:false});
    });
    cdp.on('Network.responseReceived',e=>{
      const row=rows.get(e.requestId);if(!row)return;const h=Object.fromEntries(Object.entries(e.response.headers || {}).map(([k,v])=>[k.toLowerCase(),v]));
      Object.assign(row,{status:e.response.status,protocol:e.response.protocol,content_type:h['content-type'] || e.response.mimeType || null,cache_control:h['cache-control'] || null,content_encoding:h['content-encoding'] || null,content_length:h['content-length'] || null,from_disk_cache:!!e.response.fromDiskCache,from_service_worker:!!e.response.fromServiceWorker});
    });
    cdp.on('Network.dataReceived',e=>{
      const row=rows.get(e.requestId);if(row){row.decoded_body_bytes+=e.dataLength;row.observed_encoded_body_bytes=(row.observed_encoded_body_bytes || 0)+(e.encodedDataLength || 0);}
      output.total_decoded_body_bytes+=e.dataLength;transferred+=e.encodedDataLength || 0;
      if(transferred>a.maxTransferBytes && !stopping){stopping=true;output.byte_budget_exceeded=true;cdp.send('Page.stopLoading').catch(()=>{});}
    });
    cdp.on('Network.loadingFinished',e=>{
      output.total_encoded_bytes+=e.encodedDataLength;
      const row=rows.get(e.requestId);if(row){row.encoded_bytes=e.encodedDataLength;row.finished=true;}
      if(output.total_encoded_bytes>a.maxTransferBytes && !stopping){stopping=true;output.byte_budget_exceeded=true;cdp.send('Page.stopLoading').catch(()=>{});}
    });
    cdp.on('Network.loadingFailed',e=>{const row=rows.get(e.requestId);if(row){row.finished=false;row.failure=e.errorText;}});
    if(a.coverage) {
      cdp.on('Page.frameNavigated',e=>{if(!e.frame.parentId)mainFrameId=e.frame.id;});
      await cdp.send('Page.enable');mainFrameId=(await cdp.send('Page.getFrameTree')).frameTree.frame.id;
      cdp.on('Runtime.executionContextCreated',e=>{if(executionContexts.size<a.maxResources)executionContexts.set(e.context.id,e.context.auxData || {});else coverageDiscoveryTruncated=true;});
      await cdp.send('Runtime.enable');
      cdp.on('Debugger.scriptParsed',e=>{if(scripts.size<a.maxResources)scripts.set(e.scriptId,e);else coverageDiscoveryTruncated=true;});
      cdp.on('CSS.styleSheetAdded',e=>{if(styles.size<a.maxResources)styles.set(e.header.styleSheetId,{...e.header,length_current:true});else coverageDiscoveryTruncated=true;});
      cdp.on('CSS.styleSheetChanged',e=>{const info=styles.get(e.styleSheetId);if(info)info.length_current=false;});
      await cdp.send('Debugger.enable');await cdp.send('Profiler.enable');await cdp.send('Profiler.startPreciseCoverage',{callCount:true,detailed:true});
      await cdp.send('DOM.enable');await cdp.send('CSS.enable');await cdp.send('CSS.startRuleUsageTracking');
    }
  } catch(e) {output.error=String(e.message);}
  return {output,async finish() {
    output.resources=[...rows.values()];output.unfinished_resource_count=output.resources.filter(x=>!x.finished).length;output.transfer_complete=!output.resources_truncated && !output.unfinished_resource_count;output.transferred_bytes_lower_bound=!output.transfer_complete;
    // Failed/unfinished requests have only observed body bytes; never claim a full total.
    for(const row of output.resources)if(!row.finished){row.encoded_bytes=row.observed_encoded_body_bytes || 0;output.total_encoded_bytes+=row.encoded_bytes;}
    let coverage=null;
    if(a.coverage) {
      coverage={status:'не удалось измерить',main_frame_id:mainFrameId,scope:'основной документ; дочерние фреймы и внутренние URL браузера исключены',unit:'кодовые единицы UTF-16; не сетевые байты',max_source_units:a.coverageMaxBytes,total_units:0,used_units:0,js:[],css:[],truncated:coverageDiscoveryTruncated || !mainFrameId,exclusions:[],errors:[]};
      const exclude=(type,url,frameId,reason)=>{if(coverage.exclusions.length<a.maxResources)coverage.exclusions.push({type,url,frame_id:frameId || null,reason});};
      if(cdp)try {
        const js=(await cdp.send('Profiler.takePreciseCoverage')).result;
        await cdp.send('Profiler.stopPreciseCoverage');
        for(const item of js) {
          const info=scripts.get(item.scriptId);const n=info?.length;
          const sourceURL=item.url || info?.url || '';
          if(!/^https?:/.test(sourceURL) || !(sourceURL===page.url() || [...rows.values()].some(row=>row.url===sourceURL && row.type==='Script')))continue;
          const scriptFrame=info?.executionContextAuxData?.frameId || executionContexts.get(info?.executionContextId)?.frameId;
          if(!scriptFrame){coverage.truncated=true;exclude('js',sourceURL,null,'Контекст или фрейм скрипта не установлен');continue;}
          if(scriptFrame!==mainFrameId){exclude('js',sourceURL,scriptFrame,'Скрипт дочернего фрейма вне популяции основного документа');continue;}
          const ranges=item.functions.flatMap(f=>f.ranges);
          if(!Number.isFinite(n) || n<=0 || coverage.total_units+n>a.coverageMaxBytes || ranges.length>10000 || coverage.js.length>=a.maxResources){coverage.truncated=true;continue;}
          const used=usedCoverageUnits(ranges,n);
          coverage.js.push({url:sourceURL,frame_id:scriptFrame,total_units:n,used_units:used});coverage.total_units+=n;coverage.used_units+=used;
        }
        const css=(await cdp.send('CSS.stopRuleUsageTracking')).ruleUsage;
        for(const [styleSheetId,info] of styles) {
          // CDP supplies the sheet's source-character length before any text retrieval.
          // Inline CSS is bounded by its own length, never by the entire HTML transfer.
          if(info.origin!=='regular')continue;
          const sourceURL=info.sourceURL || page.url();
          if(!info.frameId || !mainFrameId){coverage.truncated=true;exclude('css',sourceURL,info.frameId,'Фрейм таблицы стилей не установлен');continue;}
          if(info.frameId!==mainFrameId){exclude('css',sourceURL,info.frameId,'Таблица стилей дочернего фрейма вне популяции основного документа');continue;}
          if(!/^https?:/.test(sourceURL)){exclude('css',sourceURL,info.frameId,'Внутренний URL браузера или иной непубличный тип адреса');continue;}
          const n=info.length;
          const ranges=css.filter(x=>x.styleSheetId===styleSheetId).map(x=>({...x,count:x.used?1:0}));
          if(!Number.isSafeInteger(n) || n<0 || !info.length_current || coverage.total_units+n>a.coverageMaxBytes || ranges.length>10000){coverage.truncated=true;continue;}
          const used=usedCoverageUnits(ranges,n);
          coverage.css.push({url:sourceURL,frame_id:info.frameId,owner_node:info.ownerNode || null,source_type:info.ownerNode?'стиль с DOM-владельцем':'отдельная таблица стилей',size_source:'CSS.CSSStyleSheetHeader.length',total_units:n,used_units:used});coverage.total_units+=n;coverage.used_units+=used;
        }
        coverage.status=coverage.total_units ? 'измерено' : 'не удалось измерить';
      } catch(e){coverage.errors.push(String(e.message));}
    }
    return coverage;
  }};
}

function collectDOM(limits) {
  const state=window.__ppAudit || {lcp:null,shifts:[],longTasks:[]};
  let maximum=0,total=0,start=0,last=0;
  for(const s of state.shifts){if(s.at-last>1000 || s.at-start>5000){total=s.value;start=s.at;}else total+=s.value;last=s.at;maximum=Math.max(maximum,total);}
  const nav=performance.getEntriesByType('navigation')[0],fcp=performance.getEntriesByName('first-contentful-paint')[0];
  const els=[],walker=document.createTreeWalker(document.body || document.documentElement,NodeFilter.SHOW_ELEMENT);
  let next;while(els.length<limits.maxDomElements && (next=walker.nextNode()))els.push(next);
  const truncated=!!walker.nextNode();
  const visible=el=>{
    const s=getComputedStyle(el),b=el.getBoundingClientRect();
    if(!b.width || !b.height || s.visibility!=='visible' || s.display==='none' || Number(s.opacity)===0)return false;
    for(let p=el.parentElement;p;p=p.parentElement){const ps=getComputedStyle(p);if(ps.display==='none' || ps.visibility!=='visible' || Number(ps.opacity)===0)return false;}
    return true;
  };
  const fixed=els.flatMap(el=>{const s=getComputedStyle(el),b=el.getBoundingClientRect();return ['fixed','sticky'].includes(s.position) && b.width>innerWidth*.5 && b.top<innerHeight && b.bottom>0 && visible(el)?[{tag:el.tagName,id:el.id,text:el.innerText?.slice(0,100),top:b.top,height:b.height,width:b.width}]:[];}).slice(0,30);
  const main=document.querySelector('main') || document.querySelector('article') || document.body;
  const fragment_ids=els.filter(el=>el.id).map(el=>el.id).slice(0,limits.maxLinks);
  const links=els.filter(el=>el.matches('a[href]')).slice(0,limits.maxLinks).map(el=>{
    let u;try{u=new URL(el.href,location.href);}catch{}
    let fragment=null,target_exists=null;
    if(u?.hash && u.origin===location.origin && u.pathname===location.pathname && u.search===location.search){try{fragment=decodeURIComponent(u.hash.slice(1));}catch{fragment=u.hash.slice(1);}target_exists=fragment==='' || !!document.getElementById(fragment) || [...document.getElementsByName(fragment)].some(e=>e.tagName==='A');}
    return {href:el.href,text:(el.innerText || el.getAttribute('aria-label') || '').slice(0,250),visible:visible(el),fragment,target_exists};
  });
  const tap=els.filter(el=>el.matches('a[href],button,input:not([type="hidden"]),select,textarea,[role="button"]') && visible(el));
  const candidates=tap.flatMap(el=>{const b=el.getBoundingClientRect();return b.width<24 || b.height<24?[{tag:el.tagName,href:el.href || null,text:(el.innerText || el.getAttribute('aria-label') || '').slice(0,150),width:b.width,height:b.height}]:[];}).slice(0,100);
  let visible_chars=0,small_font_chars=0,sum=0,min=null;
  // Count only direct text nodes, so nested spans cannot inflate text weighting.
  for(const el of els){if(!visible(el) || el.matches('script,style,noscript,template'))continue;const n=[...el.childNodes].filter(x=>x.nodeType===Node.TEXT_NODE).map(x=>x.textContent.replace(/\s+/g,' ').trim()).join('').length;if(!n)continue;const size=parseFloat(getComputedStyle(el).fontSize);if(!Number.isFinite(size))continue;visible_chars+=n;sum+=n*size;if(size<12)small_font_chars+=n;min=min===null?size:Math.min(min,size);}
  const canvas=document.createElement('canvas'),measure=canvas.getContext('2d');if(measure)measure.font='20px Arial';
  const description=document.querySelector('meta[name="description" i]')?.content || '';
  const title_pixel_width=measure?measure.measureText(document.title).width:null;
  const images=els.filter(e=>e.tagName==='IMG').slice(0,100).map(im=>({src:im.currentSrc || im.src,loading:im.loading,fetchpriority:im.getAttribute('fetchpriority'),width:im.width,height:im.height,rendered_width:im.getBoundingClientRect().width,rendered_height:im.getBoundingClientRect().height,naturalWidth:im.naturalWidth,naturalHeight:im.naturalHeight,srcset:im.srcset,sizes:im.sizes,visible:visible(im)}));
  const main_text=main?.innerText?.slice(0,60000) || '';
  return {lcp_ms:state.lcp?.ms ?? null,lcp_element:state.lcp,cls:maximum,fcp_ms:fcp?.startTime ?? null,ttfb_ms:nav ? nav.responseStart-nav.requestStart : null,long_tasks:state.longTasks,
    dom:{title:document.title,title_pixel_width,head:{title:document.title,title_pixel_width,description_pixel_width:measure?measure.measureText(description).width:null,title_width_threshold_px:600,measurement_font:'20px Arial; диагностический ориентир, не фактический поисковый сниппет'},
      canonical:[...document.querySelectorAll('link[rel~="canonical" i]')].map(e=>e.href),meta_robots:[...document.querySelectorAll('meta[name="robots" i],meta[name="googlebot" i]')].map(e=>({name:e.name,content:e.content})),viewport:[...document.querySelectorAll('meta[name="viewport" i]')].map(e=>e.content),
      h1:els.filter(e=>e.tagName==='H1').slice(0,100).map(e=>e.innerText.slice(0,5000)),main_text,overflow_px:Math.max(0,document.documentElement.scrollWidth-innerWidth),fixed,images,links,fragment_ids,
      tap_targets:{measured:tap.length,candidates,threshold_px:24,candidate_count:tap.filter(el=>{const b=el.getBoundingClientRect();return b.width<24 || b.height<24;}).length},
      text_metrics:{visible_chars,small_font_chars,small_font_share:visible_chars?small_font_chars/visible_chars:null,min_font_px:min,weighted_font_px:visible_chars?sum/visible_chars:null,small_font_threshold_px:12},
      element_count:els.length,elements_truncated:truncated,links_truncated:els.filter(e=>e.matches('a[href]')).length>limits.maxLinks,
      content_present:!!main_text.trim() || images.some(im=>im.visible && im.naturalWidth>0)}};
}

async function run(a) {
  const dir = path.resolve(a.audit);
  const outputPath=path.join(dir,'raw',a.outputName),partialPath=outputPath.replace(/\.json$/,'.partial.json');
  if (fs.existsSync(outputPath)) throw Error('Браузерный срез уже существует; создайте новый HTTP-аудит для повторной проверки');
  const manifest = JSON.parse(fs.readFileSync(path.join(dir,'raw/manifest.json'),'utf8'));
  const pages = JSON.parse(fs.readFileSync(path.join(dir,'raw/pages.json'),'utf8'));
  const site = new URL(manifest.site);
  const eligible = pages.filter(r=>r.status===200 && r.page && !r.error && !r.truncated);
  let urls;
  if (a.urls) {
    urls = a.urls.split(',').map(normalized);
    if (urls.some(u=>!eligible.some(r=>normalized(r.requested_url)===u))) throw Error('URL должен иметь разрешённый успешный HTTP-срез');
  } else {
    const templates = new Set(); urls = [];
    for (const r of eligible) {
      const u=new URL(r.requested_url); const t=u.pathname.split('/').filter(Boolean)[0] || 'home';
      if (!templates.has(t)) {templates.add(t);urls.push(r.requested_url);}
      if (urls.length>=a.maxPages) break;
    }
  }
  if (urls.length>a.maxPages || !urls.length) throw Error('Нет допустимых URL или превышен --max-pages');
  const robotCache = new Map();
  function robotsAllowed(url) {
    if (robotCache.has(url)) return robotCache.get(url);
    const u = new URL(url);
    const policy = manifest.robots.find(p=>p.row && new URL(p.row.requested_url).protocol===u.protocol);
    if (!policy || policy.state==='доступ не подтверждён') return false;
    const body = policy.row.raw_file ? fs.readFileSync(path.join(dir,policy.row.raw_file),'utf8') : '';
    const py = spawnSync(process.env.AUDIT_PYTHON || 'python3', ['-c',
      'import json,sys,urllib.robotparser; d=json.load(sys.stdin); p=urllib.robotparser.RobotFileParser(); p.parse(d["body"].splitlines()); print("yes" if p.can_fetch("PPWebsiteAudit/0.1",d["url"]) else "no")'],
      {input:JSON.stringify({body,url}),encoding:'utf8'});
    if (py.status!==0) throw Error('Не удалось проверить robots через Python');
    const ok = py.stdout.trim()==='yes'; robotCache.set(url,ok); return ok;
  }
  let chromium;
  try {({chromium} = require('playwright'));} catch {throw Error('Playwright недоступен. Укажите NODE_PATH к установленным пакетам; автоматической установки нет.');}
  const launch = {headless:true};
  if (a.chrome || process.env.AUDIT_CHROME) launch.executablePath = a.chrome || process.env.AUDIT_CHROME;
  const browser = await chromium.launch(launch);
  const results = {version:'0.2.2',at:new Date().toISOString(),browser:browser.version(),config:{timeout_ms:a.timeout,window_ms:a.window,max_requests:a.maxRequests,max_resources:a.maxResources,max_transfer_bytes:a.maxTransferBytes,max_dom_elements:a.maxDomElements,max_links:a.maxLinks,coverage:a.coverage,coverage_max_source_units:a.coverageMaxBytes},runs:[],
    limitations:['Диагностическое наблюдение с инструментальной задержкой DNS/robots guard; не самостоятельная приёмка скорости.', 'Лабораторное наблюдение за заданное окно без Lighthouse/INP.', 'GET/HEAD только; формы и покупки не выполнялись.',
      'Снимки и геометрия требуют предметного review; профиль не имитирует автоматически slow mobile сеть/CPU.', 'Лимит сетевых байтов останавливает загрузку после CDP-сигнала; возможен ограниченный транспортный перелёт. Заголовки cookies и авторизации не сохраняются.', 'Размер текста взвешен числом видимых символов; маленькая зона касания — кандидат, пространственные исключения требуют проверки.', 'Покрытие JS/CSS — отдельный диагностический профиль внутри серии: такая серия исключена из приёмки скорости; неизвестные/слишком большие источники пропускаются.']};
  const allowedHosts = new Map();
  async function allowedPublic(url) {
    const u=new URL(url);
    if (!['http:','https:'].includes(u.protocol) || u.username || u.password) return false;
    if (allowedHosts.has(u.hostname)) return allowedHosts.get(u.hostname);
    try {
      const addresses=await dns.lookup(u.hostname.replace(/^\[|\]$/g,''), {all:true});
      const ok=addresses.length>0 && addresses.every(r=>publicIP(r.address,a.allowLocal));
      allowedHosts.set(u.hostname,ok);return ok;
    } catch {return false;}
  }
  try {
    for (const url of urls) for (const width of a.widths) for (let repeat=1;repeat<=a.repeats;repeat++) {
      const profile={width,height:900,dpr:1,mobile:width<768,network:'без искусственного ограничения',cpu:'без искусственного ограничения',window_ms:a.window};
      const ctx=await browser.newContext({viewport:{width,height:900},deviceScaleFactor:1,isMobile:profile.mobile,hasTouch:profile.mobile,serviceWorkers:'block',userAgent:'PPWebsiteAudit/0.1 Browser'});
      const page=await ctx.newPage();
      const r={run_id:crypto.createHash('sha256').update(url+width+repeat+(a.coverage?'coverage':'')+a.outputName).digest('hex').slice(0,20),requested_url:url,final_url:null,profile,repeat,ok:false,navigation_ok:false,dom_usable:false,speed_clean:false,diagnostic_perturbation:!!a.coverage,same_url:false,network_failed:[],scope_blocked:[],scope_blocked_total:0,instrumentation_blocked:[],attempted_navigation:[],documents:[],resources:[],at:new Date().toISOString()};
      let requests=0; const blockedRequests=new WeakSet(); const net=await networkProbe(ctx,page,a);
      await ctx.route('**/*',async route=> {
        const req=route.request();
        const scope=classifyRequest(req,page,site,manifest);
        const block=async reason=>{const record={url:req.url(),type:req.resourceType(),method:req.method(),is_main_document:scope.is_main_document,frame_url:scope.frame_url,reason};r.scope_blocked_total++;if(r.scope_blocked.length<a.maxResources)r.scope_blocked.push(record);blockedRequests.add(req);if(scope.is_main_document){if(r.attempted_navigation.length<a.maxResources)r.attempted_navigation.push(record);}else if(r.instrumentation_blocked.length<a.maxResources)r.instrumentation_blocked.push(record);return route.abort('blockedbyclient');};
        if(net.output.byte_budget_exceeded) return block('лимит сетевых байтов');
        if (++requests>a.maxRequests) return block('лимит запросов');
        if (!['GET','HEAD'].includes(req.method())) return block('метод вне режима чтения');
        try {
          const u=new URL(req.url());
          if(scope.reason) return block(scope.reason);
          if (u.host===site.host && !robotsAllowed(req.url())) return block('robots запрещает URL или его политика недоступна');
          if (!await allowedPublic(req.url())) return block('непубличный адрес или неподтверждённый DNS');
          await route.continue();
        } catch {await block('проверка границ охвата не завершена');}
      });
      if (ctx.routeWebSocket) await ctx.routeWebSocket('**/*',ws=>ws.close());
      page.on('requestfailed',req=>{if(!blockedRequests.has(req) && r.network_failed.length<a.maxResources)r.network_failed.push({url:req.url(),type:req.resourceType(),reason:req.failure()?.errorText || 'requestfailed'});});
      page.on('response',res=>{
        const v={url:res.url(),status:res.status(),type:res.request().resourceType()};
        if(r.resources.length<a.maxResources)r.resources.push(v);
        if (v.type==='document' && r.documents.length<a.maxResources) r.documents.push(v);
        if (v.status>=400 && r.network_failed.length<a.maxResources) r.network_failed.push({url:v.url,status:v.status});
      });
      await page.addInitScript(()=>{
        window.__ppAudit={lcp:null,shifts:[],longTasks:[]};
        try {new PerformanceObserver(list=>{for(const e of list.getEntries()){const el=e.element;window.__ppAudit.lcp={ms:e.startTime,tag:el?.tagName,src:el?.currentSrc || el?.src || null,loading:el?.getAttribute('loading') || null,fetchpriority:el?.getAttribute('fetchpriority') || null,width:el?.getBoundingClientRect().width || null,height:el?.getBoundingClientRect().height || null,currentSrc:el?.currentSrc || null};}}).observe({type:'largest-contentful-paint',buffered:true});} catch {}
        try {new PerformanceObserver(list=>{for(const e of list.getEntries())if(!e.hadRecentInput && window.__ppAudit.shifts.length<1000)window.__ppAudit.shifts.push({at:e.startTime,value:e.value});}).observe({type:'layout-shift',buffered:true});} catch {}
        try {new PerformanceObserver(list=>{for(const e of list.getEntries())if(window.__ppAudit.longTasks.length<1000)window.__ppAudit.longTasks.push({at:e.startTime,duration:e.duration});}).observe({type:'longtask',buffered:true});} catch {}
      });
      try {
        const response=await page.goto(url,{waitUntil:'load',timeout:a.timeout});
        r.navigation_status=response?.status() || null;
        await page.waitForTimeout(a.window);
        r.final_url=page.url();r.same_url=normalized(url)===normalized(r.final_url);
        const data=await page.evaluate(collectDOM,{maxDomElements:a.maxDomElements,maxLinks:a.maxLinks});
        Object.assign(r,data);
        r.navigation_ok=!!r.navigation_status && r.navigation_status<400 && !r.attempted_navigation.length;
        r.dom_usable=r.navigation_ok && r.same_url && !!r.dom.content_present;
        r.ok=r.dom_usable;
        if (!r.navigation_ok) r.error='Навигация основного документа не прошла границы охвата или HTTP-проверку';
        else if(!r.dom_usable)r.error='DOM не принадлежит заданному URL или не содержит измеримого содержимого';
        r.screenshot='raw/browser-'+r.run_id+'.png';
        try {await page.screenshot({path:path.join(dir,r.screenshot),fullPage:false,timeout:a.timeout});}
        catch(e){r.screenshot_error=String(e.message);r.screenshot=null;}
      } catch(e) {r.error=String(e.message);r.final_url=page.url();}
      r.coverage=await net.finish();r.network=net.output;
      if(r.dom)for(const im of r.dom.images){const resource=r.network.resources.find(x=>x.url===im.src);if(resource)Object.assign(im,{encoded_bytes:resource.encoded_bytes,content_type:resource.content_type,cache_control:resource.cache_control});}
      await ctx.close();
      r.network.unfinished_resource_count=r.network.resources.filter(x=>!x.finished).length;
      r.network.transfer_complete=!r.network.resources_truncated && !r.network.unfinished_resource_count;
      r.network.transferred_bytes_lower_bound=!r.network.transfer_complete;
      for(const resource of r.network.resources) {
        let resourceURL;try{resourceURL=new URL(resource.url);}catch{}
        if(!resource.finished && resource.type==='Other' && resource.initiator_type==='other' && resourceURL?.origin===new URL(url).origin && resourceURL.pathname==='/favicon.ico' && resource.status===null && resource.failure==='net::ERR_ABORTED' && !resource.observed_encoded_body_bytes) {
          resource.speed_exclusion_reason='Браузер отменил автоматический запрос favicon до ответа; не является отказом ресурса основного документа';
        }
      }
      r.network.speed_blocking_unfinished_resources=r.network.resources.filter(x=>!x.finished && !x.speed_exclusion_reason).length;
      r.speed_clean=r.dom_usable && !r.network_failed.length && !r.diagnostic_perturbation && !r.network.byte_budget_exceeded && !r.scope_blocked.length && r.network.supported && !r.network.resources_truncated && !r.network.speed_blocking_unfinished_resources;
      results.runs.push(r);
      fs.writeFileSync(partialPath,JSON.stringify(results,null,2));
      process.stdout.write(JSON.stringify({url,width,repeat,navigation_ok:r.navigation_ok,dom_usable:r.dom_usable,speed_clean:r.speed_clean})+'\n');
    }
  } finally {await browser.close();}
  fs.renameSync(partialPath,outputPath);
  process.stdout.write('Сбор завершён. Пересоберите отчёт: audit_site.py --out <каталог> --render-only\n');
}

if(require.main===module) {
  if(process.argv.includes('--help')) process.stdout.write('Браузерный сбор: --audit <каталог> [--urls <URL,URL>] [--widths 360,412,1365] [--repeats 3] [--window 5000] [--max-pages 3] [--max-requests 200] [--output-name browser.json] [--max-resources 200] [--max-transfer-bytes 20971520] [--max-dom-elements 15000] [--max-links 1000] [--coverage yes|no] [--coverage-max-bytes 2097152] [--chrome <путь>] [--allow-local]\n');
  else {
    try {run(argsOf(process.argv.slice(2))).catch(e=>{process.stderr.write(e.message+'\n');process.exitCode=1;});}
    catch(e) {process.stderr.write(e.message+'\n');process.exitCode=1;}
  }
}
module.exports={argsOf,publicIP,classifyRequest,usedCoverageUnits,collectDOM};
