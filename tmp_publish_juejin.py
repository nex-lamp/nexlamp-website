#!/usr/bin/env python3
"""临时脚本：发布文章到掘金"""

import json, urllib.request, os

COOKIE_PATH = r"d:\AI共享文件夹\juejin_cookies.json"
ARTICLE_PATH = r"d:\AI共享文件夹\nexlamp-website\推广版本\2026-07-01-smart-light-standby-juejin.json"

def api_call(url, headers, data=None, method="GET"):
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8")[:500]
        print(f"API {method} {url} -> {e.code}: {err}")
        return None
    except Exception as e:
        print(f"API error: {e}")
        return None

def main():
    with open(COOKIE_PATH, "r", encoding="utf-8") as f:
        cookies = json.load(f)
    cookie_str = cookies.get("cookie_string", "")

    with open(ARTICLE_PATH, "r", encoding="utf-8") as f:
        article = json.load(f)

    headers = {
        "Cookie": cookie_str,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Referer": "https://juejin.cn/editor/drafts/new",
        "Origin": "https://juejin.cn",
    }

    # Create draft with full fields
    create_data = {
        "title": article["title"],
        "brief_content": article["brief_content"],
        "mark_content": article["mark_content"],
        "category_id": article["category_id"],
        "tag_ids": article["tag_ids"],
        "editor_type": 1,
        "link_url": "",
        "cover_image": "",
    }

    create = api_call("https://juejin.cn/content_api/v1/article_draft/create", headers,
                      data=json.dumps(create_data).encode("utf-8"), method="POST")
    if not create:
        print("掘金草稿创建失败")
        return False

    if create.get("err_no", -1) != 0:
        print(f"掘金创建失败: {create}")
        return False

    draft_id = create["data"].get("id")
    print(f"掘金草稿创建成功: {draft_id}")

    # Publish
    publish = api_call("https://juejin.cn/content_api/v1/article/publish", headers,
                       data=json.dumps({"draft_id": draft_id}).encode("utf-8"), method="POST")
    if not publish:
        print("掘金发布请求失败")
        return False

    if publish.get("err_no") != 0:
        print(f"掘金发布失败: {publish}")
        return False

    article_id = publish["data"].get("article_id")
    print(f"掘金发布成功: article_id={article_id}")
    return True

if __name__ == "__main__":
    main()
