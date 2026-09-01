# 第二题，用re.findall提取所有以flag{}包裹的内容（包括flag{}本身）
import re

def extract_flags(s):
    return re.findall(r"flag{.+?}",s)

print(extract_flags("aa flag{abc123} bb flag{xyz}"))

