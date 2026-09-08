import requests

url = "http://ctflab.iytzx.com"
resp = requests.get(url)
print(f'状态码：', resp.status_code)
print(f'服务：', resp.headers["Server"])
print(resp.text[:200])
