# **第 2 题：** 写函数 `clean(s)`，去掉字符串两端空白，全部转小写，把空格替换成下划线。

"""def clean(s):
    s = s.strip()
    s = s.lower()
    s = s.replace(" ", "_")
    return s
print(clean("  aBc dE fg  "))"""

def clean(s):
    s = s.strip().lower().replace(" ", "_")
    return s
print(clean("  aBc dE fg  "))