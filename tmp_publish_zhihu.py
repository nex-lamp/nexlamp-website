#!/usr/bin/env python3
"""临时脚本：发布文章到知乎（优先API，失败转Playwright）"""

import json, urllib.request, urllib.parse, os, subprocess, sys

AUTH_PATH = r"d:\AI共享文件夹\zhihu_auth_state.json"
ARTICLE_PATH = r"d:\AI共享文件夹\nexlamp-website\推广版本\2026-07-01-smart-light-standby-wechat-zhihu.md"

def load_cookies():
    with open(AUTH_PATH, "r", encoding="utf-8") as f:
        state = json.load(f)
    cookies = state.get("cookies", [])
    cookie_dict = {c["name"]: c["value"] for c in cookies}
    cookie_str = "; ".join([f"{k}={v}" for k, v in cookie_dict.items()])
    return cookie_dict, cookie_str

def api_call(url, headers, data=None, method="GET"):
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"API {method} {url} -> {e.code}: {e.read().decode('utf-8')[:300]}")
        return None
    except Exception as e:
        print(f"API error: {e}")
        return None

def publish_api():
    cookie_dict, cookie_str = load_cookies()
    xsrf = cookie_dict.get("_xsrf", "")
    if not xsrf:
        # also try d_c0
        xsrf = cookie_dict.get("d_c0", "")

    headers = {
        "Cookie": cookie_str,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Referer": "https://zhuanlan.zhihu.com/write",
        "Origin": "https://zhuanlan.zhihu.com",
        "X-XSRF-TOKEN": xsrf,
    }

    # Verify auth
    me = api_call("https://www.zhihu.com/api/v4/me", headers)
    if not me:
        print("知乎 cookie 验证失败")
        return False
    print("知乎登录用户:", me.get("name"))

    # Read article
    with open(ARTICLE_PATH, "r", encoding="utf-8") as f:
        md = f.read()
    # Simple front matter strip
    if md.startswith("#"):
        lines = md.split("\n")
        title = lines[0].lstrip("# ").strip()
        content = "\n".join(lines[1:]).strip()
    else:
        title = "智能灯待机耗电实测：为什么你家灯没开，电表还在转？"
        content = md

    # Create draft
    draft_data = {
        "title": title,
        "content": content,
    }
    draft = api_call("https://zhuanlan.zhihu.com/api/articles/drafts", headers,
                     data=json.dumps(draft_data).encode("utf-8"), method="POST")
    if not draft:
        print("创建知乎草稿失败")
        return False

    draft_id = draft.get("id")
    print(f"知乎草稿创建成功: {draft_id}")

    # Publish
    publish = api_call(f"https://zhuanlan.zhihu.com/api/articles/{draft_id}/publish", headers,
                       data=json.dumps({}).encode("utf-8"), method="PUT")
    if publish:
        print("知乎发布成功")
        return True
    else:
        print("知乎发布失败")
        return False

if __name__ == "__main__":
    ok = publish_api()
    sys.exit(0 if ok else 1)
