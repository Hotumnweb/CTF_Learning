# 第 3 题： 写函数 split_join(s)，把字符串按空格切开成列表，再用 - 拼回去。

def split_join(s):
    q = s.split(" ")
    return "-".join(q)

print(split_join("ab cd ef g"))