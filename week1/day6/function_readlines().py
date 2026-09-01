# **第 2 题：** 用 `readlines()` 读取，返回每行组成的列表（注意去掉每行末尾的 `\n`，用 strip）。

def read_lines(filename):
    result = []
    with open(filename,'r') as f:
        file = f.readlines()
        for i in file:
            result.append(i.strip())
    return result
print(read_lines("data.txt"))