# 写函数 `is_even(n)`，n 是偶数返回 `True`，奇数返回 `False`

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
print(is_even(18))