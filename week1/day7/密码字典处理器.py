"""
1. 逐行读取
2. 去掉每行空白（strip）
3. 跳过空行
4. 全部转小写
5. **去重**（相同的词只保留一个，提示：可以用 list 配合 `if word not in result`，或者用 set）
6. 把清理后的结果写入新文件并排序
"""
def clean_wordlist(input_file, output_file):
    result = []
    with open(input_file,'r',encoding='utf-8') as f:
        for ch in f:
            line = ch.strip().lower()

            if line == "":
                continue
            if line not in result:
                result.append(line)
    result.sort()

    with open(output_file,'w',encoding='utf-8') as fi:
        for line in result:
            fi.write(line + '\n')

print(clean_wordlist("wordlist.txt", "clean.txt"))