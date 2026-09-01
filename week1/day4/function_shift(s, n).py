# **第 5 题：** 写函数 `shift(s, n)`，把字符串里每个字母的 ASCII 码加 n，返回新字符串（凯撒密码的雏形）。

def shift(s, n):
    result = ""
    for ch in s:
        re = chr(ord(ch) + n)
        result += re
    return result
print(shift("abc",1))
