# - `square(n)` 返回 n 的平方
# - `cube(n)` 返回 n 的立方
# - `sum_sq_cu(a, b)` 返回 `square(a) + cube(b)`（在内部调用前两个函数）

def square(n):
    return n ** 2

def cube(n):
    return n ** 3

def sum_sq_cu(a,b):
    return square(a) + cube(b)

print(sum_sq_cu(2,3))
