# **第 4 题（实战）：** 写函数 `batch_check(urls)`，批量请求 URL 列表，每个都用 try 包住，
# 成功打印状态码，失败打印 "连接失败" 并继续下一个。故意混入一个不存在的地址测试。

import requests

def batch_check(urls):
    results = []  # 存储所有结果
    for url in urls:
        try:
            resp = requests.get(url, timeout=5)
            results.append({url: resp.status_code})
        except Exception as e:
            results.append({url: f"错误: {e}"})
    return results
print(batch_check([
    "https://www.iytzx.com",
    "https://iytzx.com/sort?sortId=5",
    "http://ctf.iytzx.com",
    "http://ctflab.iytzx.com"
]))