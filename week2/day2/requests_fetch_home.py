# **第 1 题：** 请求你自己的 CTF Lab 首页，打印状态码、Server 响应头、响应正文的前 300 个字符。
import requests

def fetch_home(url):
    resp = requests.get(url)
    print('状态码：', resp.status_code)
    print('服务：', resp.headers["Server"])
    re_code = resp.text[:300]
    return re_code
print(fetch_home("http://ctflab.iytzx.com"))