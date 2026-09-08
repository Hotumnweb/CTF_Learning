# **第 1 题：** 写函数 `add_to_list(lst, item)`，如果 item 不在列表里就添加进去（去重添加），返回列表。
def add_to_list(lst, item):
    if item not in lst:
        lst.append(item)
    else:
        return lst
print(add_to_list([1, 2, 3], 2))  # [1, 2, 3]（已存在，不重复加）
print(add_to_list([1, 2, 3], 4))  # [1, 2, 3, 4]