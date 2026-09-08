import requests

url = "http://ctflab.iytzx.com/HTTP_Test.php"

def check(resp, keywords, name):
    # keywords 是通关时页面才会出现的文字，命中任意一个就算通过
    ok = any(k in resp.text for k in keywords)
    print(f"{name}: {'✅ 通关' if ok else '❌ 未通关'}")

# 关卡1：POST
r1 = requests.post(url, data={"msg": "hello_requests"})
check(r1, ["收到 POST 的 msg"], "关卡1 POST提交")

# 关卡2+3：请求头
headers = {"User-Agent": "CTF-Scanner/1.0", "X-Forwarded-For": "127.0.0.1"}
r23 = requests.get(url, headers=headers)
check(r23, ["UA 已伪装成功"], "关卡2 伪造UA")
check(r23, ["已被识别为本地"], "关卡3 伪造XFF")

# 关卡4：Cookie
r4 = requests.get(url, cookies={"auth": "admin"})
check(r4, ["Cookie auth=admin 已收到"], "关卡4 Cookie")

# 关卡5：Session两步
s = requests.Session()
s.post(url, data={"login": "1"})
r5 = s.get(url)
check(r5, ["登录状态已保持"], "关卡5 Session")
