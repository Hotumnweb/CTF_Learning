# **第 2 题：** 写函数 `safe_get(d, key)`，安全取字典的值，键不存在返回 `"无此键"`（用异常处理，不用 .get）。

def safe_get(d, key):
    try:
        return d[key]
    except KeyError:
        return "无此键"

print(safe_get({"a": 1}, "a"))  # 1
print(safe_get({"a": 1}, "b"))  # 无此键