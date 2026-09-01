# 写函数 `calc_area(r)`，计算圆面积（用 `math.pi`）
import math
def calc_area(r):
    result = math.pi * r ** 2
    return result
print(f'半径为4的圆的面积为{calc_area(4):.2f}')