#!/usr/bin/env node
/* Optional Playwright collector. No forms, clicks, logins or website edits. */
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const dns = require('node:dns').promises;
const {spawnSync} = require('node:child_process');

function argsOf(argv) {
  const a = {widths: '360,412,1365', repeats: 3, window: 5000, timeout: 20000, maxRequests: 200, maxPages: 3};
  for (let i=0; i<argv.length; i++) {
    if (!argv[i].startsWith('--')) throw Error('Нужны именованные аргументы');
    const k = argv[i].slice(2);
    if (k === 'allow-local') {a.allowLocal = true; continue;}
    if (i+1 === argv.length) throw Error('Нет значения: '+k);
    a[k] = argv[++i];
  }
  if (!a.audit) throw Error('Нужен --audit <каталог HTTP-аудита>');
  a.repeats = Number(a.repeats); a.window = Number(a.window); a.timeout = Number(a.timeout);
  a.maxRequests = Number(a['max-requests'] || a.maxRequests); a.maxPages = Number(a['max-pages'] || a.maxPages);
  a.widths = a.widths.split(',').map(Number);
  if (a.repeats < 3 || a.repeats > 10 || a.window < 1000 || a.window > 30000 || a.maxPages < 1 || a.maxPages > 20 || a.maxRequests < 1 ||
      a.widths.some(w=>w<320 || w>2560)) throw Error('Некорректные лимиты: repeats 3–10, window 1000–30000, pages 1–20, widths 320–2560');
  return a;
}

function publicIP(ip, allowLocal) {
  const py=spawnSync(process.env.AUDIT_PYTHON || 'python3',['-c',
    'import json,sys,ipaddress; d=json.load(sys.stdin); a=ipaddress.ip_address(d["ip"]); a=getattr(a,"ipv4_mapped",None) or a; print("yes" if a.is_global or (d["local"] and a.is_loopback) else "no")'],
    {input:JSON.stringify({ip,local:!!allowLocal}),encoding:'utf8'});
  return py.status===0 && py.stdout.trim()==='yes';
}

const normalized = s => {const u=new URL(s); u.hash=''; return u.href;};

async function run(a) {
  const dir = path.resolve(a.audit);
  if (fs.existsSync(path.join(dir,'raw/browser.json'))) throw Error('Браузерный срез уже существует; создайте новый HTTP-аудит для повторной проверки');
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
  const results = {version:'0.1.0',at:new Date().toISOString(),browser:browser.version(),runs:[],
    limitations:['Диагностическое наблюдение с инструментальной задержкой DNS/robots guard; не самостоятельная приёмка скорости.', 'Лабораторное наблюдение за заданное окно без Lighthouse/INP.', 'GET/HEAD только; формы и покупки не выполнялись.',
      'Снимки и геометрия требуют предметного review; профиль не имитирует автоматически slow mobile сеть/CPU.']};
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
      const r={run_id:crypto.createHash('sha256').update(url+width+repeat).digest('hex').slice(0,20),requested_url:url,final_url:null,profile,repeat,ok:false,same_url:false,network_failed:[],scope_blocked:[],documents:[],resources:[],at:new Date().toISOString()};
      let requests=0;
      await ctx.route('**/*',async route=> {
        const req=route.request();
        const block=async reason=>{r.scope_blocked.push({url:req.url(),type:req.resourceType(),reason});return route.abort('blockedbyclient');};
        if (++requests>a.maxRequests) return block('лимит запросов');
        if (!['GET','HEAD'].includes(req.method())) return block('метод вне режима чтения');
        try {
          const u=new URL(req.url());
          if (req.resourceType()==='document' && u.host!==site.host) return block('документ другого хоста вне охвата');
          if (req.resourceType()==='document' && u.search && !manifest.config.include_query) return block('параметрический документ вне охвата');
          if (u.host===site.host && !robotsAllowed(req.url())) return block('robots запрещает URL или его политика недоступна');
          if (!await allowedPublic(req.url())) return block('непубличный адрес или неподтверждённый DNS');
          await route.continue();
        } catch {await block('проверка границ охвата не завершена');}
      });
      if (ctx.routeWebSocket) await ctx.routeWebSocket('**/*',ws=>ws.close());
      page.on('requestfailed',req=>r.network_failed.push({url:req.url(),reason:req.failure()?.errorText || 'requestfailed'}));
      page.on('response',res=>{
        const v={url:res.url(),status:res.status(),type:res.request().resourceType()};
        r.resources.push(v);
        if (v.type==='document') r.documents.push(v);
        if (v.status>=400) r.network_failed.push({url:v.url,status:v.status});
      });
      await page.addInitScript(()=>{
        window.__ppAudit={lcp:null,shifts:[],longTasks:[]};
        try {new PerformanceObserver(list=>{for(const e of list.getEntries()){const el=e.element;window.__ppAudit.lcp={ms:e.startTime,tag:el?.tagName,src:el?.currentSrc || el?.src || null,loading:el?.getAttribute('loading') || null};}}).observe({type:'largest-contentful-paint',buffered:true});} catch {}
        try {new PerformanceObserver(list=>{for(const e of list.getEntries())if(!e.hadRecentInput)window.__ppAudit.shifts.push({at:e.startTime,value:e.value});}).observe({type:'layout-shift',buffered:true});} catch {}
        try {new PerformanceObserver(list=>{for(const e of list.getEntries())window.__ppAudit.longTasks.push({at:e.startTime,duration:e.duration});}).observe({type:'longtask',buffered:true});} catch {}
      });
      try {
        const response=await page.goto(url,{waitUntil:'load',timeout:a.timeout});
        r.navigation_status=response?.status() || null;
        await page.waitForTimeout(a.window);
        r.final_url=page.url();r.same_url=normalized(url)===normalized(r.final_url);
        const data=await page.evaluate(()=>{
          const state=window.__ppAudit || {lcp:null,shifts:[],longTasks:[]};
          let maximum=0,total=0,start=0,last=0;
          for(const s of state.shifts){if(s.at-last>1000 || s.at-start>5000){total=s.value;start=s.at;}else total+=s.value;last=s.at;maximum=Math.max(maximum,total);}
          const nav=performance.getEntriesByType('navigation')[0];
          const fcp=performance.getEntriesByName('first-contentful-paint')[0];
          const fixed=[...document.querySelectorAll('body *')].flatMap(el=>{
            const s=getComputedStyle(el),b=el.getBoundingClientRect();
            return ['fixed','sticky'].includes(s.position) && b.width>innerWidth*.5 && b.height>0 && b.top<innerHeight && b.bottom>0 && s.visibility!=='hidden' && s.display!=='none' ?
              [{tag:el.tagName,id:el.id,text:el.innerText?.slice(0,100),top:b.top,height:b.height,width:b.width}]:[];
          }).slice(0,30);
          const main=document.querySelector('main') || document.querySelector('article') || document.body;
          return {lcp_ms:state.lcp?.ms || null,lcp_element:state.lcp,cls:maximum,fcp_ms:fcp?.startTime || null,
            ttfb_ms:nav ? nav.responseStart-nav.requestStart : null,long_tasks:state.longTasks,
            dom:{title:document.title,h1:[...document.querySelectorAll('h1')].map(e=>e.innerText),main_text:main?.innerText?.slice(0,60000) || '',
              overflow_px:Math.max(0,document.documentElement.scrollWidth-innerWidth),fixed,images:[...document.images].slice(0,100).map(im=>({src:im.currentSrc,loading:im.loading,width:im.width,naturalWidth:im.naturalWidth}))}};
        });
        Object.assign(r,data);
        r.screenshot='raw/browser-'+r.run_id+'.png';
        await page.screenshot({path:path.join(dir,r.screenshot),fullPage:false});
        r.ok=!r.scope_blocked.some(x=>x.type==='document');
        if (!r.ok) r.error='Документ вне разрешённого охвата; конечное содержимое не считается измерением сайта';
      } catch(e) {r.error=String(e.message);r.final_url=page.url();}
      await ctx.close();
      results.runs.push(r);
      fs.writeFileSync(path.join(dir,'raw/browser.partial.json'),JSON.stringify(results,null,2));
      process.stdout.write(JSON.stringify({url,width,repeat,clean:r.ok && r.same_url && !r.network_failed.length})+'\n');
    }
  } finally {await browser.close();}
  fs.renameSync(path.join(dir,'raw/browser.partial.json'),path.join(dir,'raw/browser.json'));
  process.stdout.write('Сбор завершён. Пересоберите отчёт: audit_site.py --out <каталог> --render-only\n');
}

if(require.main===module) {
  if(process.argv.includes('--help')) process.stdout.write('Браузерный сбор: --audit <каталог> [--urls <URL,URL>] [--widths 360,412,1365] [--repeats 3] [--window 5000] [--max-pages 3] [--max-requests 200] [--chrome <путь>] [--allow-local]\n');
  else {
    try {run(argsOf(process.argv.slice(2))).catch(e=>{process.stderr.write(e.message+'\n');process.exitCode=1;});}
    catch(e) {process.stderr.write(e.message+'\n');process.exitCode=1;}
  }
}
module.exports={argsOf,publicIP};
