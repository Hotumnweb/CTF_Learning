# **第 2 题：** 用 `params` 字典给你的站点发带参数的 GET 请求，参数 `id=1` 和 `user=admin`，打印最终请求的 URL（`resp.url`）。

import requests

def fetch_with_params(url):
    resp = requests.get(url, params={"id":1,"user":"admin"})
    print(resp.status_code)
    return resp.url

print(fetch_with_params("http://ctflab.iytzx.com"))