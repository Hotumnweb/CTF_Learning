# 写函数 `reverse_str(s)`，返回反转后的字符串（不能用切片 [::-1]，用循环写）

def reverse_str(s):
    result = ""
    for i in range(len(s)-1, -1, -1):
        result = result + s[i]
    return result
print(reverse_str('ilovepython'))

"""
len(s) 返回字符串长度，比如 "hello" 长度是 5。但字符串下标从 0 开始，所以最后一个字符的下标是 5 - 1 = 4。len(s)-1 就是拿到最后一个字符的位置。
- 开始：`len(s)-1`，从最后一个字符的位置开始
- 结束：`-1`，倒着走到 0 就停（range 不包含结束值，所以写 - 1 才能包含 0）
- 步长：`-1`，每次减 1，也就是倒着走
以 `"hello"`（长度 5）为例，这个 range 生成的就是：`4, 3, 2, 1, 0`，正好从最后一个字符取到第一个。
`result = result + s[i]` 就是对的。它的意思是：把当前字符 `s[i]` 拼到 result 后面。每循环一次，result 就多一个字符，循环结束就拼出了完整的反转字符串。
"""