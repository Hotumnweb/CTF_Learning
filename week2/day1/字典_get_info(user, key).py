# **第 2 题：** 给定一个用户字典，写函数 `get_info(user, key)`，用 `.get()` 安全取值，键不存在返回 `"未知"`。

def get_info(user, key):
    return user.get(key,"未知")

u = {"name": "admin", "role": "administrator"}
print(get_info(u, "name"))  # admin
print(get_info(u, "email"))  # 未知