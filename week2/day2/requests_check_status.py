# **第 3 题（小工具）：** 写函数 `check_status(urls)`，输入一个 URL 列表，逐个请求，
# 返回每个 URL 的状态码字典 `{url: 状态码}`。
import requests

def check_status(urls):
    result = {}
    for url in urls:
        resp = requests.get(url)
        result[url] = resp.status_code
    return result
print(check_status(["http://ctflab.iytzx.com", "http://ctflab.iytzx.com/notexist"]))