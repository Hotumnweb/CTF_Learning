# **第 3 题：** 写函数 `safe_div(a, b)`，做除法，除数为 0 时返回 `"不能除以0"`。

def safe_div(a,b):
   try:
       return a/b
   except ZeroDivisionError:
       return "不能除以0"

print(safe_div(10, 2))  # 5.0
print(safe_div(10, 0))  # 不能除以0
