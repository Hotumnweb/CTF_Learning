# 写函数 `count_char(s, c)`，统计字符 c 在字符串 s 中出现的次数

def count_char(s, c):
    result = 0
    for i in s:
        if i == c:
            result += 1
    return result

print(count_char('hello','o'))