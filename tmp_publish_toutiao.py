#!/usr/bin/env python3
"""临时脚本：发布微头条和文章到今日头条"""

import subprocess, json, os

WORKSPACE = "C:/Users/yu/.workbuddy/binaries/node/workspace"
COVER_URL = "https://www.nexlamp.com/images/blog-2026-07-01-cover.png"

def run(args):
    env = os.environ.copy()
    env["NODE_PATH"] = "./node_modules"
    cmd = [os.path.join(WORKSPACE, "node_modules/.bin/toutiao-ops.cmd")] + args
    result = subprocess.run(
        cmd,
        cwd=WORKSPACE,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=180,
    )
    print("STDOUT:", result.stdout[-1000:] if len(result.stdout) > 1000 else result.stdout)
    print("STDERR:", result.stderr[-1000:] if len(result.stderr) > 1000 else result.stderr)
    print("EXIT:", result.returncode)
    return result.returncode == 0

weitoutiao_content = """装完全屋智能灯，电费多了几十块，我一开始以为是冰箱空调。结果拿功率计一测，发现灯明明关了，居然还在偷偷耗电。普通LED灯关灯是真断电，0W。但有些Wi-Fi智能灯待机要0.8W-1.5W，廉价方案甚至2W-4W。20盏灯一年下来，待机电费能差出100多块。最坑的是为了兼容可控硅调光，关灯后还让可控硅微导通，灯会出现"鬼火"微亮。建议选灯时看看待机功耗，优先Zigbee/Matter。已经装完的朋友可以买个功率计测一遍。"""

article_path = r"d:\AI共享文件夹\nexlamp-website\推广版本\2026-07-01-smart-light-standby-toutiao-article.md"
with open(article_path, "r", encoding="utf-8") as f:
    article_content = f.read()

print("=== 发布微头条 ===")
ok1 = run([
    "publish", "weitoutiao",
    "--content", weitoutiao_content
])

print("\n=== 发布文章 ===")
ok2 = run([
    "publish", "article",
    "--title", "智能灯待机耗电实测：为什么你家灯没开，电表还在转？",
    "--content", article_content,
    "--cover", COVER_URL
])

print(f"\n微头条: {'成功' if ok1 else '失败'}")
print(f"文章: {'成功' if ok2 else '失败'}")
