# 第一题，用re.findall提取字符串里所有的数字
import re

def extract_numbers(s):
    return re.findall(r"\d+",s)

print(extract_numbers("abc123def45g6"))