# **第 4 题：** 写函数 `find_flag(s)`，查找 `"flag"` 在字符串中的位置，找不到返回 -1。

def find_flag(s):
    re = s.find("flag")
    return re

print(find_flag("xxflag{test}"))
print(find_flag("nothing here"))