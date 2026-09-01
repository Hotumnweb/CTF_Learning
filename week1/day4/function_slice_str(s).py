# **第 1 题：** 写函数 `slice_str(s)`，返回一个元组，包含：前 3 个字符、后 3 个字符、每隔 2 个字符取一个。

"""
def slice_str(s):
    a = s[:3]
    b = s[-3:]
    c = s[::2]
    d = ",".join([a, b, c])
    return d

print(slice_str("abcdefghij"))
"""
def slice_str(s):
    return s[:3],s[-3:],s[::2]
print(slice_str("abcdefghij"))