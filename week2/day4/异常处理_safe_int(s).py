# **第 1 题：** 写函数 `safe_int(s)`，尝试把字符串转成整数，转换失败就返回 `-1` 而不是崩溃。

def safe_int(s):
    try:
        return int(s)
    except ValueError:
        return -1

print(safe_int("123"))
print(safe_int("abc"))