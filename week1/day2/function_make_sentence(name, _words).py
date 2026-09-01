# 写函数 `make_sentence(name, *words)`，把 name 和后面所有词拼成一句话。
# 比如 `make_sentence("小明", "我", "爱", "CTF")` 返回 `"小明：我爱CTF"`。

def make_sentence(name, *words):
    result = ""
    for i in words:
        result += i
    return f'{name}:{result}'
print(make_sentence('小明', '我', '爱', 'CTF'))
