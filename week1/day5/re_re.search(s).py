# 用re.search提取flag{}花括号里面的内容（用花括号分组，group（1））
import re

def get_inside(s):
    return re.search(r"flag{(.+?)}",s).group(1)
print(get_inside("result=flag{h3110_w0rld}&end"))