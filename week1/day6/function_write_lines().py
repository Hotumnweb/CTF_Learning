# **第 4 题：** 把一个列表写入新文件 `result.txt`，每个元素占一行。

def write_lines(filename, lines):
    with open(filename,'w',encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')

print(write_lines("result.txt", ["apple", "banana", "orange"]))