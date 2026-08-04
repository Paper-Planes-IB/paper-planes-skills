#!/usr/bin/env python3
import argparse
import json
import math
import os
import re
from collections import Counter, defaultdict, deque
from datetime import datetime, timezone


def load_graph(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    nodes = data.get("nodes", [])
    links = data.get("links") or data.get("edges") or []
    by_id = {n.get("id"): n for n in nodes if n.get("id")}
    adj = defaultdict(list)
    for e in links:
        s, t = e.get("source"), e.get("target")
        if not s or not t:
            continue
        adj[s].append((t, e))
        adj[t].append((s, e))
    return data, nodes, links, by_id, adj


def inferred_type(node):
    node_type = node.get("node_type")
    if node_type:
        return node_type
    role = node.get("node_role")
    if role == "project_god":
        return "project"
    if role == "cross_project_hub":
        return "hub"
    if node.get("artifact_kind"):
        return "artifact"
    file_type = node.get("file_type")
    if file_type in {"document", "paper", "image", "code"}:
        return "artifact"
    if file_type in {"concept", "rationale"}:
        return "concept"
    return "unknown"


def label_match(by_id, query):
    if query in by_id:
        return query
    q = query.casefold()
    exact = [i for i, n in by_id.items() if str(n.get("label", "")).casefold() == q]
    if exact:
        return exact[0]
    contains = [i for i, n in by_id.items() if q in str(n.get("label", "")).casefold()]
    if len(contains) == 1:
        return contains[0]
    if contains:
        return contains[0]
    raise SystemExit(f"Node not found: {query}")


def degree_counter(links):
    c = Counter()
    for e in links:
        if e.get("source"):
            c[e["source"]] += 1
        if e.get("target"):
            c[e["target"]] += 1
    return c


def components(by_id, adj):
    seen = set()
    comps = []
    for node_id in by_id:
        if node_id in seen:
            continue
        q = deque([node_id])
        seen.add(node_id)
        comp = []
        while q:
            cur = q.popleft()
            comp.append(cur)
            for nxt, _ in adj.get(cur, []):
                if nxt not in seen:
                    seen.add(nxt)
                    q.append(nxt)
        comps.append(comp)
    return comps


def project_nodes(nodes):
    return [n for n in nodes if inferred_type(n) == "project" or n.get("node_role") == "project_god"]


def hub_nodes(nodes):
    return [n for n in nodes if inferred_type(n) == "hub" or n.get("node_role") == "cross_project_hub"]


def normalize_label(label):
    text = str(label or "").casefold()
    text = text.replace("ё", "е")
    text = re.sub(r"^проект:\s*", "", text)
    text = re.sub(r"[^0-9a-zа-я]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def node_neighbor_set(node_id, adj, by_id, include_hubs=True, include_artifacts=True):
    out = set()
    for neighbor, _ in adj.get(node_id, []):
        t = inferred_type(by_id.get(neighbor, {}))
        if t == "project":
            continue
        if t == "hub" and not include_hubs:
            continue
        if t == "artifact" and not include_artifacts:
            continue
        out.add(neighbor)
    return out


def jaccard(left, right):
    if not left and not right:
        return 0.0
    union = left | right
    if not union:
        return 0.0
    return len(left & right) / len(union)


def print_table(rows, headers):
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))
    print(" | ".join(h.ljust(widths[i]) for i, h in enumerate(headers)))
    print(" | ".join("-" * widths[i] for i in range(len(headers))))
    for row in rows:
        print(" | ".join(str(cell).ljust(widths[i]) for i, cell in enumerate(row)))


def cmd_inspect(args):
    data, nodes, links, by_id, adj = load_graph(args.graph)
    comps = components(by_id, adj)
    deg = degree_counter(links)
    roles = Counter(inferred_type(n) for n in nodes)
    relations = Counter(e.get("relation", "") for e in links)
    stale_days = None
    try:
        mtime = os.path.getmtime(args.graph)
        stale_days = (datetime.now(timezone.utc) - datetime.fromtimestamp(mtime, timezone.utc)).days
    except OSError:
        pass
    out = {
        "nodes": len(nodes),
        "edges": len(links),
        "components": len(comps),
        "largest_component": max((len(c) for c in comps), default=0),
        "project_nodes": len(project_nodes(nodes)),
        "hub_nodes": len(hub_nodes(nodes)),
        "types": dict(roles),
        "relations": dict(relations),
        "graph_age_days": stale_days,
        "top_degree": [(by_id[i].get("label", i), d) for i, d in deg.most_common(args.limit)],
    }
    if args.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return
    print(f"Nodes: {out['nodes']}")
    print(f"Edges: {out['edges']}")
    print(f"Components: {out['components']} (largest: {out['largest_component']})")
    print(f"Project God nodes: {out['project_nodes']}")
    print(f"Cross-project hubs: {out['hub_nodes']}")
    if stale_days is not None:
        print(f"Graph age: {stale_days} day(s)")
    print("\nTypes:", ", ".join(f"{k}={v}" for k, v in roles.most_common()))
    print("Relations:", ", ".join(f"{k}={v}" for k, v in relations.most_common(10)))
    print("\nTop degree:")
    for label, d in out["top_degree"]:
        print(f"- {label}: {d}")


def cmd_list_gods(args):
    _, nodes, links, by_id, adj = load_graph(args.graph)
    deg = degree_counter(links)
    rows = []
    for n in project_nodes(nodes):
        contains = sum(1 for _, e in adj.get(n["id"], []) if e.get("relation") == "project_contains")
        hubs = sum(1 for neighbor, _ in adj.get(n["id"], []) if inferred_type(by_id.get(neighbor, {})) == "hub")
        rows.append((n.get("label", n["id"]), deg[n["id"]], contains, hubs, n.get("project", "")))
    rows.sort(key=lambda r: (-r[1], r[0]))
    if args.json:
        print(json.dumps([dict(label=r[0], degree=r[1], contains=r[2], hubs=r[3], project=r[4]) for r in rows], ensure_ascii=False, indent=2))
    else:
        print_table(rows[: args.limit], ["project God node", "degree", "contains", "hubs", "project"])


def cmd_list_hubs(args):
    _, nodes, links, by_id, adj = load_graph(args.graph)
    deg = degree_counter(links)
    rows = []
    for n in hub_nodes(nodes):
        projects = sorted({by_id[neighbor].get("label", neighbor) for neighbor, _ in adj.get(n["id"], []) if inferred_type(by_id.get(neighbor, {})) == "project"})
        rows.append((n.get("label", n["id"]), len(projects), deg[n["id"]], ", ".join(projects[:5]) + (" ..." if len(projects) > 5 else "")))
    rows.sort(key=lambda r: (-r[1], -r[2], r[0]))
    if args.json:
        print(json.dumps([dict(label=r[0], hub_spread=r[1], degree=r[2], sample_projects=r[3]) for r in rows], ensure_ascii=False, indent=2))
    else:
        print_table(rows[: args.limit], ["hub", "hub_spread", "degree", "sample projects"])


def cmd_explain(args):
    _, nodes, links, by_id, adj = load_graph(args.graph)
    node_id = label_match(by_id, args.node)
    node = by_id[node_id]
    neighbors = adj.get(node_id, [])
    rows = []
    for other, edge in sorted(neighbors, key=lambda x: by_id.get(x[0], {}).get("label", x[0]))[: args.limit]:
        n = by_id.get(other, {"label": other})
        rows.append((n.get("label", other), inferred_type(n), edge.get("relation", ""), edge.get("confidence_score", ""), edge.get("source_file", "")))
    if args.json:
        print(json.dumps({"id": node_id, "label": node.get("label"), "type": inferred_type(node), "degree": len(neighbors), "neighbors": rows}, ensure_ascii=False, indent=2))
        return
    print(f"Node: {node.get('label', node_id)}")
    print(f"ID: {node_id}")
    print(f"Type: {inferred_type(node)}")
    print(f"Degree: {len(neighbors)}")
    if inferred_type(node) == "hub":
        print("Note: this is a cross-project hub, not a project God node.")
    print()
    print_table(rows, ["neighbor", "type", "relation", "confidence", "source"])


def bfs_path(adj, start, end, min_conf):
    q = deque([start])
    prev = {start: (None, None)}
    while q:
        cur = q.popleft()
        if cur == end:
            break
        for nxt, edge in adj.get(cur, []):
            if edge.get("confidence_score", 1.0) < min_conf:
                continue
            if nxt not in prev:
                prev[nxt] = (cur, edge)
                q.append(nxt)
    if end not in prev:
        return []
    path = []
    cur = end
    while prev[cur][0] is not None:
        parent, edge = prev[cur]
        path.append((parent, cur, edge))
        cur = parent
    return list(reversed(path))


def cmd_trace(args):
    _, nodes, links, by_id, adj = load_graph(args.graph)
    start = label_match(by_id, args.start)
    end = label_match(by_id, args.end)
    path = bfs_path(adj, start, end, args.min_confidence)
    if not path:
        print("No path found.")
        return
    if args.json:
        print(json.dumps([{"source": s, "target": t, "relation": e.get("relation"), "confidence": e.get("confidence_score")} for s, t, e in path], ensure_ascii=False, indent=2))
        return
    print(f"Path: {by_id[start].get('label')} -> {by_id[end].get('label')}")
    for i, (s, t, e) in enumerate(path, 1):
        print(f"{i}. {by_id[s].get('label', s)} --{e.get('relation')} ({e.get('confidence_score', '')})--> {by_id[t].get('label', t)}")


def cmd_ego(args):
    _, nodes, links, by_id, adj = load_graph(args.graph)
    start = label_match(by_id, args.node)
    seen = {start}
    q = deque([(start, 0)])
    order = []
    while q:
        cur, depth = q.popleft()
        order.append((cur, depth))
        if depth >= args.depth:
            continue
        for nxt, edge in adj.get(cur, []):
            if edge.get("confidence_score", 1.0) < args.min_confidence:
                continue
            if nxt not in seen:
                seen.add(nxt)
                q.append((nxt, depth + 1))
    rows = [(depth, by_id[i].get("label", i), inferred_type(by_id[i]), len(adj.get(i, [])), by_id[i].get("source_file", "")) for i, depth in order]
    if args.json:
        print(json.dumps([dict(depth=r[0], label=r[1], type=r[2], degree=r[3], source_file=r[4]) for r in rows], ensure_ascii=False, indent=2))
    else:
        print_table(rows[: args.limit], ["depth", "node", "type", "degree", "source"])


def cmd_validate(args):
    _, nodes, links, by_id, adj = load_graph(args.graph)
    issues = []
    node_ids = set(by_id)
    comps = components(by_id, adj)
    isolated = [n for n in nodes if len(adj.get(n.get("id"), [])) == 0]
    low_conf_count = 0
    missing_as_of_count = 0
    missing_source_count = 0
    for n in nodes:
        t = inferred_type(n)
        label = n.get("label", n.get("id"))
        if t == "project" and not str(label).startswith("Проект:"):
            issues.append(("god_node_rule", label))
        if t == "hub" and str(label).startswith("Проект:"):
            issues.append(("hub_is_project_named", label))
        if not n.get("node_type") and not n.get("node_role"):
            if t in {"project", "hub", "unknown"}:
                issues.append(("missing_type_role", label))
    for e in links:
        if e.get("source") not in node_ids or e.get("target") not in node_ids:
            issues.append(("dangling_edge", f"{e.get('source')} -> {e.get('target')}"))
        if e.get("confidence_score", 1.0) < args.min_confidence:
            low_conf_count += 1
            issues.append(("low_confidence_edge", f"{e.get('source')} -> {e.get('target')} ({e.get('confidence_score')})"))
        if not e.get("as_of") and not e.get("captured_at"):
            missing_as_of_count += 1
        if not e.get("source_file") and not e.get("source"):
            missing_source_count += 1
    for n in project_nodes(nodes):
        contains = sum(1 for _, e in adj.get(n["id"], []) if e.get("relation") == "project_contains")
        if contains < 3:
            issues.append(("under_connected_project", f"{n.get('label')} contains={contains}"))
    for n in hub_nodes(nodes):
        projects = {neighbor for neighbor, _ in adj.get(n["id"], []) if inferred_type(by_id.get(neighbor, {})) == "project"}
        if len(projects) < args.min_hub_spread:
            issues.append(("low_hub_spread", f"{n.get('label')} hub_spread={len(projects)}"))
    if nodes:
        orphan_ratio = len(isolated) / len(nodes)
        if orphan_ratio > args.orphan_yellow:
            issues.append(("orphan_ratio", f"{orphan_ratio:.1%} isolated nodes ({len(isolated)}/{len(nodes)})"))
    if links:
        low_conf_ratio = low_conf_count / len(links)
        no_as_of_ratio = missing_as_of_count / len(links)
        no_source_ratio = missing_source_count / len(links)
        if low_conf_ratio > args.low_conf_yellow:
            issues.append(("low_confidence_ratio", f"{low_conf_ratio:.1%} low-confidence edges"))
        if no_as_of_ratio > args.no_as_of_yellow:
            issues.append(("missing_as_of_ratio", f"{no_as_of_ratio:.1%} edges without as_of/captured_at"))
        if no_source_ratio > 0.1:
            issues.append(("missing_source_ratio", f"{no_source_ratio:.1%} edges without source/source_file"))
    if args.json:
        print(json.dumps({
            "nodes": len(nodes),
            "edges": len(links),
            "components": len(comps),
            "isolated_nodes": len(isolated),
            "low_confidence_edges": low_conf_count,
            "missing_as_of_edges": missing_as_of_count,
            "missing_source_edges": missing_source_count,
            "issues": [{"issue": i, "detail": d} for i, d in issues],
        }, ensure_ascii=False, indent=2))
        return
    if not issues:
        print("Graph quality: OK")
    else:
        print(f"Graph quality issues: {len(issues)}")
        for issue, detail in issues[: args.limit]:
            print(f"- {issue}: {detail}")


def cmd_components(args):
    _, nodes, links, by_id, adj = load_graph(args.graph)
    comps = sorted(components(by_id, adj), key=len, reverse=True)
    rows = []
    for idx, comp in enumerate(comps[: args.limit], 1):
        projects = [by_id[i].get("label", i) for i in comp if inferred_type(by_id[i]) == "project"]
        hubs = [by_id[i].get("label", i) for i in comp if inferred_type(by_id[i]) == "hub"]
        rows.append((idx, len(comp), len(projects), ", ".join(projects[:5]) + (" ..." if len(projects) > 5 else ""), ", ".join(hubs[:5]) + (" ..." if len(hubs) > 5 else "")))
    if args.json:
        print(json.dumps([dict(component=r[0], nodes=r[1], projects=r[2], sample_projects=r[3], sample_hubs=r[4]) for r in rows], ensure_ascii=False, indent=2))
    else:
        print_table(rows, ["component", "nodes", "projects", "sample projects", "sample hubs"])


def cmd_vip(args):
    _, nodes, links, by_id, adj = load_graph(args.graph)
    hubs = {n["id"] for n in hub_nodes(nodes)}
    project_ids = {n["id"] for n in project_nodes(nodes)}
    score = Counter()
    neighbor_projects = defaultdict(set)
    for e in links:
        s, t = e.get("source"), e.get("target")
        if not s or not t or s in hubs or t in hubs:
            continue
        if s not in project_ids:
            score[s] += 1
        if t not in project_ids:
            score[t] += 1
        if s in project_ids and t not in project_ids:
            neighbor_projects[t].add(s)
        if t in project_ids and s not in project_ids:
            neighbor_projects[s].add(t)
    rows = []
    for node_id, degree in score.most_common():
        n = by_id[node_id]
        if inferred_type(n) == "hub":
            continue
        rows.append((n.get("label", node_id), inferred_type(n), degree, len(neighbor_projects[node_id]), n.get("project", ""), n.get("source_file", "")))
        if len(rows) >= args.limit:
            break
    if args.json:
        print(json.dumps([dict(node=r[0], type=r[1], non_hub_degree=r[2], project_neighbors=r[3], project=r[4], source=r[5]) for r in rows], ensure_ascii=False, indent=2))
    else:
        print_table(rows, ["VIP node without hubs", "type", "degree", "project links", "project", "source"])


def cmd_enrich_next(args):
    _, nodes, links, by_id, adj = load_graph(args.graph)
    rows = []
    for n in project_nodes(nodes):
        pid = n["id"]
        contains = sum(1 for _, e in adj.get(pid, []) if e.get("relation") == "project_contains")
        hubs = sum(1 for neighbor, _ in adj.get(pid, []) if inferred_type(by_id.get(neighbor, {})) == "hub")
        semantic = sum(1 for neighbor, _ in adj.get(pid, []) if by_id.get(neighbor, {}).get("project") == n.get("project") and inferred_type(by_id.get(neighbor, {})) in {"concept", "artifact"})
        has_local_graph = "yes" if semantic > 15 and contains > 15 else "maybe"
        priority = (hubs + 1) / max(semantic, 1)
        rows.append((priority, n.get("label", pid), hubs, contains, semantic, has_local_graph))
    rows.sort(key=lambda r: (-r[0], r[1]))
    out = rows[: args.limit]
    if args.json:
        print(json.dumps([dict(priority=round(r[0], 3), project=r[1], hubs=r[2], contains=r[3], semantic_neighbors=r[4], enriched=r[5]) for r in out], ensure_ascii=False, indent=2))
    else:
        print_table([(round(r[0], 3), r[1], r[2], r[3], r[4], r[5]) for r in out], ["priority", "project", "hubs", "contains", "semantic", "enriched"])


def cmd_monoculture(args):
    _, nodes, links, by_id, adj = load_graph(args.graph)
    rows = []
    for n in project_nodes(nodes):
        hub_edges = []
        for neighbor, edge in adj.get(n["id"], []):
            if inferred_type(by_id.get(neighbor, {})) == "hub":
                hub_edges.append((neighbor, edge))
        if not hub_edges:
            continue
        counts = Counter(neighbor for neighbor, _ in hub_edges)
        top_hub, top_count = counts.most_common(1)[0]
        share = top_count / len(hub_edges)
        if share >= args.threshold:
            rows.append((round(share, 2), n.get("label", n["id"]), by_id[top_hub].get("label", top_hub), len(hub_edges)))
    rows.sort(key=lambda r: (-r[0], r[1]))
    if args.json:
        print(json.dumps([dict(share=r[0], project=r[1], dominant_hub=r[2], hub_edges=r[3]) for r in rows[: args.limit]], ensure_ascii=False, indent=2))
    else:
        print_table(rows[: args.limit], ["share", "project", "dominant hub", "hub edges"])


def cmd_compare(args):
    _, nodes, links, by_id, adj = load_graph(args.graph)
    left = label_match(by_id, args.left)
    right = label_match(by_id, args.right)
    left_neighbors = node_neighbor_set(left, adj, by_id, include_hubs=True, include_artifacts=args.include_artifacts)
    right_neighbors = node_neighbor_set(right, adj, by_id, include_hubs=True, include_artifacts=args.include_artifacts)
    common = left_neighbors & right_neighbors
    common_rows = []
    for nid in sorted(common, key=lambda x: by_id.get(x, {}).get("label", x))[: args.limit]:
        n = by_id.get(nid, {"label": nid})
        common_rows.append((n.get("label", nid), inferred_type(n), len(adj.get(nid, [])), n.get("source_file", "")))
    out = {
        "left": by_id[left].get("label", left),
        "right": by_id[right].get("label", right),
        "jaccard": jaccard(left_neighbors, right_neighbors),
        "left_neighbors": len(left_neighbors),
        "right_neighbors": len(right_neighbors),
        "common_neighbors": len(common),
        "common": common_rows,
    }
    if args.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return
    print(f"Compare: {out['left']} <> {out['right']}")
    print(f"Jaccard: {out['jaccard']:.3f} ({out['common_neighbors']} common / {out['left_neighbors']} and {out['right_neighbors']} neighbors)")
    print()
    print_table(common_rows, ["common neighbor", "type", "degree", "source"])


def cmd_weak_nodes(args):
    _, nodes, links, by_id, adj = load_graph(args.graph)
    rows = []
    comp_index = {}
    for idx, comp in enumerate(components(by_id, adj), 1):
        for node_id in comp:
            comp_index[node_id] = (idx, len(comp))
    for n in nodes:
        node_id = n.get("id")
        degree = len(adj.get(node_id, []))
        comp_id, comp_size = comp_index.get(node_id, ("", 0))
        if degree <= args.max_degree or comp_size <= args.max_component_size:
            rows.append((degree, comp_size, n.get("label", node_id), inferred_type(n), n.get("project", ""), n.get("source_file", "")))
    rows.sort(key=lambda r: (r[0], r[1], r[2]))
    if args.json:
        print(json.dumps([dict(degree=r[0], component_size=r[1], node=r[2], type=r[3], project=r[4], source=r[5]) for r in rows[: args.limit]], ensure_ascii=False, indent=2))
    else:
        print_table(rows[: args.limit], ["degree", "component", "weak node", "type", "project", "source"])


def cmd_duplicates(args):
    _, nodes, links, by_id, adj = load_graph(args.graph)
    buckets = defaultdict(list)
    generic_exact_labels = {
        "00 карточка проекта",
        "карточка проекта",
        "трекер задач",
        "карта чатов",
        "codex project task inbox",
        "bpm storyline storyboard",
        "storyline storyboard",
    }
    for n in nodes:
        key = normalize_label(n.get("label", n.get("id")))
        if key:
            buckets[key].append(n.get("id"))
    rows = []
    for ids in buckets.values():
        if len(ids) < 2:
            continue
        for i, left in enumerate(ids):
            for right in ids[i + 1 :]:
                score = jaccard(node_neighbor_set(left, adj, by_id), node_neighbor_set(right, adj, by_id))
                left_type = inferred_type(by_id[left])
                right_type = inferred_type(by_id[right])
                if not args.include_generic and score < args.min_neighbor_similarity and left_type != "project" and right_type != "project":
                    continue
                if not args.include_generic and normalize_label(by_id[left].get("label")) in generic_exact_labels and score < args.min_neighbor_similarity:
                    continue
                rows.append((1.0, score, by_id[left].get("label", left), by_id[right].get("label", right), left, right, "same_normalized_label"))
    if args.fuzzy:
        indexed = [(n.get("id"), normalize_label(n.get("label", n.get("id")))) for n in nodes]
        for i, (left, left_label) in enumerate(indexed):
            left_tokens = set(left_label.split())
            if not left_tokens:
                continue
            for right, right_label in indexed[i + 1 :]:
                right_tokens = set(right_label.split())
                if not right_tokens:
                    continue
                token_score = jaccard(left_tokens, right_tokens)
                if token_score >= args.min_label_similarity:
                    neighbor_score = jaccard(node_neighbor_set(left, adj, by_id), node_neighbor_set(right, adj, by_id))
                    if neighbor_score >= args.min_neighbor_similarity:
                        rows.append((token_score, neighbor_score, by_id[left].get("label", left), by_id[right].get("label", right), left, right, "fuzzy_label_and_neighbors"))
    rows.sort(key=lambda r: (-r[0], -r[1], r[2], r[3]))
    if args.json:
        print(json.dumps([dict(label_similarity=round(r[0], 3), neighbor_jaccard=round(r[1], 3), left=r[2], right=r[3], left_id=r[4], right_id=r[5], reason=r[6]) for r in rows[: args.limit]], ensure_ascii=False, indent=2))
    else:
        print("Duplicate candidates only. Do not merge without human approval.")
        print_table([(round(r[0], 3), round(r[1], 3), r[2], r[3], r[4], r[5], r[6]) for r in rows[: args.limit]], ["label sim", "neighbor sim", "left", "right", "left id", "right id", "reason"])


def articulation_points(by_id, adj):
    time = 0
    disc = {}
    low = {}
    parent = {}
    result = set()

    def dfs(u):
        nonlocal time
        children = 0
        time += 1
        disc[u] = low[u] = time
        for v, _ in adj.get(u, []):
            if v not in disc:
                parent[v] = u
                children += 1
                dfs(v)
                low[u] = min(low[u], low[v])
                if parent.get(u) is None and children > 1:
                    result.add(u)
                if parent.get(u) is not None and low[v] >= disc[u]:
                    result.add(u)
            elif v != parent.get(u):
                low[u] = min(low[u], disc[v])

    for node_id in by_id:
        if node_id not in disc:
            parent[node_id] = None
            dfs(node_id)
    return result


def cmd_bridges(args):
    _, nodes, links, by_id, adj = load_graph(args.graph)
    arts = articulation_points(by_id, adj)
    deg = degree_counter(links)
    rows = []
    for node_id in arts:
        n = by_id[node_id]
        neighbor_projects = sorted({by_id[neighbor].get("label", neighbor) for neighbor, _ in adj.get(node_id, []) if inferred_type(by_id.get(neighbor, {})) == "project"})
        if args.require_project_spread and len(neighbor_projects) < 2:
            continue
        rows.append((deg[node_id], len(neighbor_projects), n.get("label", node_id), inferred_type(n), ", ".join(neighbor_projects[:5]) + (" ..." if len(neighbor_projects) > 5 else ""), n.get("source_file", "")))
    rows.sort(key=lambda r: (-r[1], -r[0], r[2]))
    if args.json:
        print(json.dumps([dict(degree=r[0], project_spread=r[1], node=r[2], type=r[3], sample_projects=r[4], source=r[5]) for r in rows[: args.limit]], ensure_ascii=False, indent=2))
    else:
        print_table(rows[: args.limit], ["degree", "project spread", "bridge candidate", "type", "sample projects", "source"])


def relation_weight(edge):
    relation = edge.get("relation", "")
    if relation == "project_contains":
        return 1.0
    if relation == "uses_cross_project_hub":
        return 0.55
    if relation in {"implements", "rationale_for", "evidence_for"}:
        return 0.9
    if relation in {"conceptually_related_to", "semantically_similar_to"}:
        return 0.75
    if relation == "references":
        return 0.6
    return 0.5


def link_prediction_features(left, right, adj, by_id, generic_hub_degree):
    left_neighbors = {n for n, _ in adj.get(left, []) if inferred_type(by_id.get(n, {})) != "project"}
    right_neighbors = {n for n, _ in adj.get(right, []) if inferred_type(by_id.get(n, {})) != "project"}
    common = left_neighbors & right_neighbors
    union = left_neighbors | right_neighbors
    if not common or not union:
        return None
    weighted_common = 0.0
    adamic_adar = 0.0
    specific_common = 0
    shared = []
    for nid in common:
        degree = max(len(adj.get(nid, [])), 1)
        node = by_id.get(nid, {})
        node_type = inferred_type(node)
        generic_hub = node_type == "hub" and degree >= generic_hub_degree
        if not generic_hub:
            specific_common += 1
        type_factor = 0.25 if generic_hub else (0.55 if node_type == "hub" else 1.0)
        incident = [e for n, e in adj.get(left, []) if n == nid] + [e for n, e in adj.get(right, []) if n == nid]
        edge_factor = sum(relation_weight(e) for e in incident) / max(len(incident), 1)
        contribution = type_factor * edge_factor / math.log(degree + 2)
        weighted_common += contribution
        adamic_adar += 1 / math.log(degree + 2)
        shared.append((contribution, node.get("label", nid), inferred_type(node), degree))
    jaccard = len(common) / len(union)
    score = weighted_common + (jaccard * 2.0)
    shared.sort(reverse=True)
    return {
        "common_neighbors": len(common),
        "jaccard": jaccard,
        "adamic_adar": adamic_adar,
        "specific_common": specific_common,
        "score": score,
        "shared": shared,
    }


def cmd_link_predict(args):
    _, nodes, links, by_id, adj = load_graph(args.graph)
    project_ids = [n["id"] for n in project_nodes(nodes)]
    existing = {tuple(sorted((e.get("source"), e.get("target")))) for e in links if e.get("source") and e.get("target")}
    rows = []
    for i, left in enumerate(project_ids):
        for right in project_ids[i + 1 :]:
            if tuple(sorted((left, right))) in existing:
                continue
            features = link_prediction_features(left, right, adj, by_id, args.generic_hub_degree)
            if not features:
                continue
            if features["score"] < args.min_score or features["common_neighbors"] < args.min_common:
                continue
            if not args.allow_generic_only and features["specific_common"] == 0:
                continue
            shared = "; ".join(f"{label} [{typ}, d={degree}]" for _, label, typ, degree in features["shared"][: args.shared_limit])
            rows.append((
                features["score"],
                features["common_neighbors"],
                features["specific_common"],
                features["jaccard"],
                by_id[left].get("label", left),
                by_id[right].get("label", right),
                args.relation,
                shared,
            ))
    rows.sort(key=lambda r: (-r[0], -r[1], r[3], r[4]))
    out = rows[: args.limit]
    if args.json:
        print(json.dumps([
            {
                "score": round(r[0], 4),
                "common_neighbors": r[1],
                "specific_common": r[2],
                "jaccard": round(r[3], 4),
                "source": r[4],
                "target": r[5],
                "suggested_relation": r[6],
                "why": r[7],
            }
            for r in out
        ], ensure_ascii=False, indent=2))
    else:
        print("Link prediction candidates only. Do not write these as graph edges without human approval.")
        print_table([
            (round(r[0], 3), r[1], r[2], round(r[3], 3), r[4], r[5], r[6], r[7])
            for r in out
        ], ["score", "common", "specific", "jaccard", "source", "target", "suggested relation", "why"])


def main():
    parser = argparse.ArgumentParser(description="Inspect Graphify/Vault graph.json files.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    for name in ["inspect", "list-gods", "list-hubs", "components", "vip", "enrich-next"]:
        p = sub.add_parser(name)
        p.add_argument("graph")
        p.add_argument("--limit", type=int, default=20)
        p.add_argument("--min-confidence", type=float, default=0.5)
        p.add_argument("--json", action="store_true")
    p = sub.add_parser("validate")
    p.add_argument("graph")
    p.add_argument("--limit", type=int, default=20)
    p.add_argument("--min-confidence", type=float, default=0.5)
    p.add_argument("--min-hub-spread", type=int, default=3)
    p.add_argument("--orphan-yellow", type=float, default=0.03)
    p.add_argument("--low-conf-yellow", type=float, default=0.2)
    p.add_argument("--no-as-of-yellow", type=float, default=0.3)
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("monoculture")
    p.add_argument("graph")
    p.add_argument("--threshold", type=float, default=0.8)
    p.add_argument("--limit", type=int, default=20)
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("explain")
    p.add_argument("graph")
    p.add_argument("node")
    p.add_argument("--limit", type=int, default=25)
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("ego")
    p.add_argument("graph")
    p.add_argument("node")
    p.add_argument("--depth", type=int, default=2)
    p.add_argument("--limit", type=int, default=80)
    p.add_argument("--min-confidence", type=float, default=0.5)
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("trace")
    p.add_argument("graph")
    p.add_argument("start")
    p.add_argument("end")
    p.add_argument("--min-confidence", type=float, default=0.5)
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("compare")
    p.add_argument("graph")
    p.add_argument("left")
    p.add_argument("right")
    p.add_argument("--include-artifacts", action="store_true")
    p.add_argument("--limit", type=int, default=30)
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("weak-nodes")
    p.add_argument("graph")
    p.add_argument("--max-degree", type=int, default=1)
    p.add_argument("--max-component-size", type=int, default=2)
    p.add_argument("--limit", type=int, default=50)
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("duplicates")
    p.add_argument("graph")
    p.add_argument("--fuzzy", action="store_true")
    p.add_argument("--include-generic", action="store_true")
    p.add_argument("--min-label-similarity", type=float, default=0.82)
    p.add_argument("--min-neighbor-similarity", type=float, default=0.2)
    p.add_argument("--limit", type=int, default=50)
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("bridges")
    p.add_argument("graph")
    p.add_argument("--require-project-spread", action="store_true")
    p.add_argument("--limit", type=int, default=30)
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("link-predict")
    p.add_argument("graph")
    p.add_argument("--limit", type=int, default=20)
    p.add_argument("--min-common", type=int, default=2)
    p.add_argument("--min-score", type=float, default=0.1)
    p.add_argument("--shared-limit", type=int, default=4)
    p.add_argument("--generic-hub-degree", type=int, default=20)
    p.add_argument("--allow-generic-only", action="store_true")
    p.add_argument("--relation", default="candidate_cross_project_review")
    p.add_argument("--json", action="store_true")
    args = parser.parse_args()
    {
        "inspect": cmd_inspect,
        "list-gods": cmd_list_gods,
        "list-hubs": cmd_list_hubs,
        "explain": cmd_explain,
        "ego": cmd_ego,
        "trace": cmd_trace,
        "validate": cmd_validate,
        "components": cmd_components,
        "vip": cmd_vip,
        "enrich-next": cmd_enrich_next,
        "monoculture": cmd_monoculture,
        "compare": cmd_compare,
        "weak-nodes": cmd_weak_nodes,
        "duplicates": cmd_duplicates,
        "bridges": cmd_bridges,
        "link-predict": cmd_link_predict,
    }[args.cmd](args)


if __name__ == "__main__":
    main()
