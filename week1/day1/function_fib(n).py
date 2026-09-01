# 写函数 `fib(n)`，返回第 n 个斐波那契数
# 规则：`fib(0)=0, fib(1)=1, fib(2)=1, fib(3)=2, fib(4)=3, fib(5)=5...`

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for i in range(2, n+1):
        next = a + b
        a = b
        b = next
    return b
print(fib(4))

"""
`n=4`，所以是 `range(2, 5)`，生成的数字是：**2, 3, 4**（不包含 5）。
为什么从 2 开始？因为 fib (0) 和 fib (1) 已经用 if 处理了，我们要从第 2 个位置开始往后算。为什么到 5 结束？因为 range 不包含结束值，写 5 才能包含 4。
## 逐轮追踪 a 和 b 的变化
初始状态：`a=0, b=1`
轮次	        i       next = a+b	a 变成	b 变成	含义
开始前     	-	    -	        0	    1       fib(0)=0, fib(1)=1
第 1 轮	    2	    0+1=1	    1	    1	    fib(2)=1
第 2 轮   	3	    1+1=2	    1	    2	    fib(3)=2
第 3 轮   	4	    1+2=3	    2	    3	    fib(4)=3
循环结束，return b，返回 3。
"""