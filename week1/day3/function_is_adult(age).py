# 写函数 `is_adult(age)` 判断是否成年（>=18 返回 True，否则 False）。
# 再写函数 `check(name, age)`，在内部调用 `is_adult`，返回 `"xxx已成年"` 或 `"xxx未成年"`。

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

def check(name, age):
    if is_adult(age) is True:
        return f"{name}已成年"
    else:
        return f"{name}未成年"
print(check('小明',17))