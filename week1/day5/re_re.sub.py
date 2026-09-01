# 用re.sub把字符串里面所有数字替换成*

import re

def hide_numbers(s):
    return re.sub(r"\d","*",s)
print(hide_numbers("tel:13812345678"))