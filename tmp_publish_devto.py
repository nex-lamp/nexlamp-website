#!/usr/bin/env python3
"""临时脚本：发布文章到 Dev.to"""

import json, urllib.request

API_KEY = "cKj98BLMNRcfsJSGGZXN5xaU"

with open(r"d:\AI共享文件夹\nexlamp-website\推广版本\2026-07-01-smart-light-standby-devto.md", "r", encoding="utf-8") as f:
    content = f.read()

# Parse front matter
lines = content.split("\n")
if lines[0].strip() == "---":
    idx = 1
    meta = {}
    while idx < len(lines) and lines[idx].strip() != "---":
        line = lines[idx]
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
        idx += 1
    body = "\n".join(lines[idx+1:]).strip()
else:
    meta = {}
    body = content

# Clean title quotes
title = meta.get("title", "").strip('"')
tags_str = meta.get("tags", "smarthome,led,iot,energyefficiency")
tags = [t.strip() for t in tags_str.split(",")][:4]

data = {
    "article": {
        "title": title,
        "body_markdown": body,
        "published": True,
        "tags": tags,
    }
}

req = urllib.request.Request(
    "https://dev.to/api/articles",
    data=json.dumps(data).encode("utf-8"),
    headers={
        "Content-Type": "application/json",
        "api-key": API_KEY,
        "User-Agent": "nexlamp-publisher/1.0",
        "Accept": "application/json",
    },
    method="POST",
)

try:
    with urllib.request.urlopen(req, timeout=60) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        print("SUCCESS:", result.get("url"))
        print("ID:", result.get("id"))
except urllib.error.HTTPError as e:
    print("FAILED:", e.code, e.read().decode("utf-8")[:500])
except Exception as e:
    print("ERROR:", str(e))
