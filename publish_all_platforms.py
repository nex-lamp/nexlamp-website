import json
import urllib.request
import urllib.error
import subprocess
import sys
import os
from datetime import datetime

LOG_FILE = r"d:\AI共享文件夹\nexlamp-website\publish-log-2026-07-06.json"

def log_result(platform, status, detail):
    entry = {
        "time": datetime.now().isoformat(),
        "platform": platform,
        "status": status,
        "detail": detail
    }
    data = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = []
    data.append(entry)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[{platform}] {status}: {detail}")

# 1. LinkedIn: check CDP Chrome first
linkedin_status = "skipped"
linkedin_detail = ""
try:
    import urllib.request
    req = urllib.request.Request("http://127.0.0.1:9222/json/version", method="GET")
    with urllib.request.urlopen(req, timeout=5) as resp:
        cdp_info = resp.read().decode("utf-8")
        linkedin_status = "would_run"
        linkedin_detail = f"CDP Chrome detected: {cdp_info[:200]}"
except Exception as e:
    linkedin_status = "skipped"
    linkedin_detail = f"CDP Chrome not running at 127.0.0.1:9222 ({type(e).__name__}). Skipping LinkedIn."
log_result("LinkedIn", linkedin_status, linkedin_detail)

# 2. Dev.to publish (English article)
devto_status = "failed"
devto_detail = ""
try:
    DEVTO_API_KEY = "cKj98BLMNRcfsJSGGZXN5xaU"
    article_path = r"d:\AI共享文件夹\nexlamp-website\posts\devto-gb30255-smart-lighting-energy-efficiency.md"
    with open(article_path, "r", encoding="utf-8") as f:
        body_markdown = f.read()

    payload = {
        "article": {
            "title": "GB 30255-2026: How China's New Energy Standard Reshapes Smart Lighting and LED Drivers",
            "published": True,
            "body_markdown": body_markdown,
            "tags": ["smartlighting", "led", "energyefficiency", "zigbee"]
        }
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://dev.to/api/articles",
        data=data,
        headers={
            "Content-Type": "application/json",
            "api-key": DEVTO_API_KEY,
            "User-Agent": "NexlampPublisher/1.0 (https://nexlamp.com)",
            "Accept": "application/json"
        },
        method="POST"
    )

    with urllib.request.urlopen(req, timeout=60) as resp:
        resp_body = resp.read().decode("utf-8")
        resp_json = json.loads(resp_body)
        url = resp_json.get("url", "unknown")
        devto_status = "success"
        devto_detail = f"Published at {url}"
except urllib.error.HTTPError as e:
    try:
        err_body = e.read().decode("utf-8")
    except Exception:
        err_body = ""
    devto_status = "failed"
    devto_detail = f"HTTP {e.code}: {err_body[:500]}"
except Exception as e:
    devto_status = "failed"
    devto_detail = f"{type(e).__name__}: {str(e)[:500]}"
log_result("Dev.to", devto_status, devto_detail)

# 3. Toutiao micro post
toutiao_status = "failed"
toutiao_detail = ""
try:
    # 200字以内、口语化、像朋友分享经历
    content = "刚入行那会儿做智能灯，觉得灯能亮、能连App就行。直到去年开始摸新国标GB 30255-2026，才发现关灯待机那点小功耗，才是后续合规的关键。现在很多方案WiFi模块常开，关灯还偷偷耗电。换成Zigbee低功耗方案，待机能干到0.3W以内。做灯的兄弟，别只看亮度参数，待机功耗也要纳入选型表了。"

    cmd = [
        r"C:\Users\yu\.workbuddy\binaries\node\versions\22.22.2\node.exe",
        r"C:\Users\yu\.workbuddy\binaries\node\workspace\node_modules\.bin\toutiao-ops",
        "publish", "weitoutiao", "--content", content
    ]
    # Use npx via node
    env = os.environ.copy()
    env["NODE_PATH"] = "./node_modules"
    result = subprocess.run(
        cmd,
        cwd=r"C:\Users\yu\.workbuddy\binaries\node\workspace",
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=120,
        env=env
    )
    if result.returncode == 0:
        toutiao_status = "success"
        toutiao_detail = result.stdout.strip()[:500]
    else:
        toutiao_status = "failed"
        toutiao_detail = f"exit {result.returncode}: {result.stderr.strip()[:500]} {result.stdout.strip()[:500]}"
except Exception as e:
    toutiao_status = "failed"
    toutiao_detail = f"{type(e).__name__}: {str(e)[:500]}"
log_result("Toutiao", toutiao_status, toutiao_detail)

# Summary
print("\n=== Publish Summary ===")
print(f"LinkedIn: {linkedin_status}")
print(f"Dev.to:   {devto_status}")
print(f"Toutiao:  {toutiao_status}")
print(f"Log saved to: {LOG_FILE}")
