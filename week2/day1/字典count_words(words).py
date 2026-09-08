# **第 3 题：** 写函数 `count_words(words)`，输入一个单词列表，统计每个单词出现次数，返回一个字典 `{单词: 次数}`。

def count_words(words):
    result = {}
    for ch in words:
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1
    return result
print(count_words(["a", "b", "a", "c", "b", "a"]))  # {'a': 3, 'b': 2, 'c': 1}