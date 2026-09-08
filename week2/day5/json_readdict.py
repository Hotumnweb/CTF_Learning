import json

def write_json(d):
    test = json.dumps(d, ensure_ascii=False,indent=2)
    with open("config.json", 'w',encoding='utf-8') as f:
        f.write(test)

    with open("config.json", 'r',encoding='utf-8')as fi:
        data = json.load(fi)
        print(data, "数据类型：", type(data))
s = {"name": "admin", "age": "21", "flag": "flag{python_json_to_dict}"}
print(write_json(s))