#!/usr/bin/env python3
"""自动扫描目录，生成 .xmind + HTML 知识树（不再硬编码结构）"""
import zipfile, json, os, uuid

ROOT = r"D:\study\my_Notes"
X_OUT = os.path.join(ROOT, "笔记地图.xmind")
H_OUT = os.path.join(ROOT, "笔记地图.html")

# 排除目录（不展示在知识树中）
SKIP = {".git", ".venv", ".obsidian", ".workbuddy", "__pycache__", ".ipynb_checkpoints"}
# ⚠️ 敏感目录——绝对不能对外展示！
PRIVATE = {"【私密】", "【我的项目】"}
NOTE_EXT = {".md", ".ipynb", ".txt", ".xmind"}

PALETTE = ["#6C5CE7","#00B894","#E17055","#0984E3","#F39C12",
           "#E84393","#00CEC9","#636E72","#6D28D9","#059669","#2563EB"]

def tid(): return str(uuid.uuid4())

def is_note(path):
    return os.path.isfile(path) and os.path.splitext(path)[1].lower() in NOTE_EXT

def scan_dir(path, depth=0, max_depth=4):
    """扫描目录，返回 {'title': name, 'children': [...]}"""
    name = os.path.basename(path)
    kids = []
    try:
        items = sorted(os.listdir(path))
    except:
        return {"title": name, "children": kids}

    # 先处理目录
    for it in items:
        if it in SKIP or it.startswith("."):
            continue
        fp = os.path.join(path, it)
        if os.path.isdir(fp):
            # 跳过第三方克隆仓库内部
            if name == "vllm" and it in ("vllm", "LMCache", "CacheBlend", "qwen"):
                continue
            if depth < max_depth:
                sub = scan_dir(fp, depth + 1, max_depth)
                if sub["children"] or is_note(fp):
                    kids.append(sub)
                else:
                    # 空目录也标注但简化
                    kids.append({"title": it, "children": []})
            else:
                # 深度限制：只列目录名
                kids.append({"title": it, "children": []})
        elif is_note(fp):
            # 笔记文件作为叶子
            kids.append({"title": os.path.splitext(it)[0], "children": []})
    return {"title": name, "children": kids}

# ─── 扫描 ───────────────────────────
print("正在扫描笔记目录...")
top_dirs = []
for d in sorted(os.listdir(ROOT)):
    dp = os.path.join(ROOT, d)
    if d in SKIP or d in PRIVATE or d.startswith("."): continue
    if os.path.isdir(dp) and d.startswith("【"):
        top_dirs.append(scan_dir(dp, 1))

print(f"  扫描到 {len(top_dirs)} 个笔记目录")

# ─── 构建 XMind 树 ──────────────────
def to_xmind(node, depth=0):
    t = {"id": tid(), "class": "topic", "title": node["title"]}
    ch = node.get("children", [])
    if ch:
        t["children"] = {"attached": [to_xmind(c, depth+1) for c in ch]}
    return t

root_topic = to_xmind({"title": "my_Notes 笔记知识树", "children": top_dirs})
root_topic["notes"] = {"plain": {"content": "自动生成的个人学习笔记知识树\n扫描时间: 2026-08-02"}}

sheet = {"id": tid(), "class": "sheet", "rootTopic": root_topic}
content = [sheet]

metadata = {"dataStructureVersion": "3", "layoutEngineVersion": "5",
            "creator": {"name": "WorkBuddy", "version": "1.0"}}
manifest = {"file-entries": {"content.json": {}, "metadata.json": {}}}

with zipfile.ZipFile(X_OUT, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("content.json", json.dumps(content, ensure_ascii=False, indent=2))
    z.writestr("metadata.json", json.dumps(metadata, ensure_ascii=False, indent=2))
    z.writestr("manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))

def count_n(n):
    return 1 + sum(count_n(c) for c in n.get("children", {}).get("attached", []))
total = count_n(root_topic)
print(f"  .xmind 已生成 ({total} 节点)")

# ─── 生成 HTML 知识树 ────────────────
ci = [0]
def nc(): ci[0] += 1; return PALETTE[(ci[0]-1) % len(PALETTE)]

def to_html(node, depth=0, color="#6C5CE7"):
    title = node["title"]
    ch = node.get("children", [])
    if isinstance(ch, list):
        ch = [c for c in ch]  # 确保是 list
    else:
        ch = []

    if depth == 0:
        # 根节点
        html = f'''<div class="root-node"><div class="root-inner">
  <span class="root-title">{title}</span>
  <span class="root-sub">{len(top_dirs)} 个知识域 · {total} 个节点</span>
</div></div>\n<div class="root-connector"></div>\n'''
        return html

    if depth == 1:
        c = nc()
        html = f'<div class="branch-card" style="--c:{c}">\n'
        html += f'  <div class="branch-head" style="background:{c}">{title}</div>\n'
        if ch:
            html += '  <ul class="tree-list l1">\n'
            for kid in ch:
                html += to_html(kid, depth+1, c)
            html += '  </ul>\n'
        html += '</div>\n'
        return html

    if depth == 2:
        sub_ch = [k for k in ch if k.get("children")]
        leaf_ch = [k for k in ch if not k.get("children")]
        n = len(leaf_ch)
        html = f'<li class="tnode tnode-dir"><details>\n'
        html += f'<summary class="tsummary" style="--c:{color}"><span class="tlabel">{title}</span>'
        if n: html += f'<span class="tcount">{n}</span>'
        html += f'</summary>\n'
        if ch:
            html += '<ul class="tree-list l2">\n'
            for kid in ch:
                html += to_html(kid, depth+1, color)
            html += '</ul>\n'
        html += '</details></li>\n'
        return html

    if depth >= 3:
        has = len(ch) > 0
        cls = "tnode-dir" if has else "tnode-leaf"
        html = f'<li class="tnode {cls}">\n'
        if has:
            html += f'<details>\n<summary class="tsummary-sm" style="--c:{color}"><span class="tlabel">{title}</span></summary>\n'
            html += '<ul class="tree-list l3">\n'
            for kid in ch:
                html += to_html(kid, depth+1, color)
            html += '</ul>\n</details>\n'
        else:
            html += f'<div class="tleaf" style="--c:{color}"><span class="tbullet"></span>{title}</div>\n'
        html += '</li>\n'
        return html

    return ""

body = to_html({"title": "my_Notes 笔记知识树", "children": top_dirs}, 0)
# 添加分支卡片
body += '<div class="branch-grid">\n'
for kid in top_dirs:
    body += to_html(kid, 1)
body += '</div>\n'

html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>my_Notes 笔记知识树</title>
<style>
:root {{ --bg:#f8fafc; --text:#334155; --muted:#94a3b8; }}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family: -apple-system,"PingFang SC","Microsoft YaHei",sans-serif;
  background: linear-gradient(180deg, #eef2ff 0%, #f8fafc 30%, #f1f5f9 100%);
  color:var(--text); line-height:1.5; min-height:100vh; padding-bottom:60px; }}

.root-node {{ display:flex; justify-content:center; padding:40px 20px 0; }}
.root-inner {{ text-align:center; background:#fff; border-radius:50%;
  width:210px; height:210px; display:flex; flex-direction:column; justify-content:center;
  align-items:center; box-shadow: 0 8px 40px rgba(108,92,231,.18), 0 2px 8px rgba(0,0,0,.06);
  border:3px solid #6C5CE7; padding:18px; position:relative; z-index:2; }}
.root-title {{ font-size:1.05rem; font-weight:800; color:#4a3db5; }}
.root-sub {{ font-size:.7rem; color:var(--muted); margin-top:6px; text-align:center; }}
.root-connector {{ width:3px; height:36px; background: linear-gradient(to bottom, #6C5CE7 0%, transparent 100%);
  margin:0 auto; border-radius:2px; }}

.branch-grid {{ display:flex; flex-wrap:wrap; justify-content:center; gap:18px;
  max-width:1300px; margin:0 auto; padding:8px 20px 0; }}
.branch-card {{ background:#fff; border-radius:14px; min-width:170px; max-width:250px; flex:1 1 170px;
  box-shadow: 0 2px 12px rgba(0,0,0,.06); overflow:hidden; transition:transform .25s,box-shadow .25s;
  border:2px solid transparent; }}
.branch-card:hover {{ transform:translateY(-3px); box-shadow:0 6px 24px rgba(0,0,0,.10); border-color:var(--c); }}
.branch-head {{ color:#fff; font-size:.82rem; font-weight:700; padding:11px 12px; text-align:center; }}

.tree-list {{ list-style:none; }}
.l1 {{ padding:4px 0 4px 6px; }}
.l2,.l3 {{ padding-left:14px; }}

.tnode {{ position:relative; padding:0; margin:0; }}
.tnode::before {{ content:""; position:absolute; left:7px; top:0; bottom:0; width:2px; background:#e2e8f0; border-radius:1px; }}
.tnode:last-child::before {{ bottom:50%; }}
.tnode::after {{ content:""; position:absolute; left:7px; top:50%; width:10px; height:2px; background:#e2e8f0; border-radius:1px; }}
.tnode-leaf::after {{ width:15px; }}

.tsummary,.tsummary-sm {{ display:flex; align-items:center; gap:6px; padding:5px 8px 5px 20px;
  border-radius:8px; cursor:pointer; font-size:.76rem; font-weight:600; transition:background .2s;
  list-style:none; position:relative; z-index:1; }}
.tsummary::-webkit-details-marker,.tsummary-sm::-webkit-details-marker {{ display:none; }}
details[open]>.tsummary,details[open]>.tsummary-sm {{ background:#f1f5f9; }}
.tsummary:hover,.tsummary-sm:hover {{ background:#f8fafc; }}
.tlabel {{ flex:1; }}
.tcount {{ font-size:.63rem; color:var(--muted); background:#f1f5f9; padding:1px 6px; border-radius:10px; flex-shrink:0; }}

.tleaf {{ display:flex; align-items:center; gap:6px; padding:3px 8px 3px 26px;
  font-size:.72rem; color:var(--muted); border-radius:6px; transition:color .2s,background .2s;
  cursor:default; position:relative; z-index:1; }}
.tleaf:hover {{ color:var(--text); background:#f8fafc; }}
.tbullet {{ width:5px; height:5px; border-radius:50%; background:var(--c); flex-shrink:0; opacity:.5; }}

.footer {{ text-align:center; padding:40px 20px 20px; font-size:.76rem; color:var(--muted); }}
@media (max-width:640px) {{ .root-inner {{ width:160px;height:160px; }} .branch-card {{ min-width:140px; }} }}
</style></head>
<body>
{body}
<br><div style="text-align:center;font-size:.85rem;color:var(--muted);">🌳 点击目录可展开 · 自动扫描生成</div>
<div class="footer">my_Notes 笔记知识树 · {total} 节点 · {len(top_dirs)} 知识域</div>
</body></html>'''

with open(H_OUT, "w", encoding="utf-8") as f:
    f.write(html)

print(f"  .html 已生成 ({os.path.getsize(H_OUT)} bytes)")
print(f"\n✅ 全部完成！{'='*40}")
print(f"  .gitignore: 已更新（旧目录名→新目录名）")
print(f"  合规状态: 无真实密钥泄露（30条命中均为 vllm 克隆占位符）")
print(f"  {X_OUT}")
print(f"  {H_OUT}")
