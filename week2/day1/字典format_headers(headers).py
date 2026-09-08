# **第 4 题：** 写函数 `format_headers(headers)`，输入一个字典，遍历 items ()，把每个键值对格式化成 `"Key: Value"` 的列表返回。

def format_headers(headers):
    result = []
    for key, value in headers.items():
        result.append(f'{key}: {value}')
    return result

h = {"User-Agent": "Mozilla", "Accept": "text/html"}
print(format_headers(h))