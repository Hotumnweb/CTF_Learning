# **第 1 题：** 用 `with open` 一次性读取整个文件，打印内容。

def read_all(filename):
    with open(filename, 'r') as f:
        return f.read()

print(read_all("data.txt"))
