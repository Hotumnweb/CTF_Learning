# 写函数 `average(*nums)`，返回所有传入数字的平均值。不传参数时返回 `0`。

def average(*nums):
    if len(nums) == 0:
        return 0
    result = sum(nums) / len(nums)
    return result
print(average(2, 4, 6))   # 4.0
print(average(10, 20))    # 15.0
print(average())          # 0