# 写函数 `max_of_three(a, b, c)`，返回三个数中的最大值（不能用 max ()）

def max_of_three(a,b,c):
    biggest = a
    if b > biggest:
        biggest = b
    if c >biggest:
        biggest = c
    return biggest
print(f'最大的是{max_of_three(20,5,8)}')

"""
**return 的位置确实关键** — 如果 return 
缩进到 if 里面，那条件不满足时函数就没有 return，Python 默认返回 `None`。
这就是为什么 return 要放在函数体最后、和 if 同级。
第二个 if 缩进太深了，它嵌套在了第一个 if 里面。意思是：只有当 `b > a` 成立时，才会去比较 c。如果 b 比 a 小，c 根本不会被检查。
"""