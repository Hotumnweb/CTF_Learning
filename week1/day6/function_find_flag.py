# **第 3 题：** 在文件里找到包含 `flag` 的那一行并返回。

def find_flag_line(filename):
    with open(filename,'r',encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if "flag" in line:
                return line.strip()
print(find_flag_line("data.txt"))