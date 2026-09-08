import json

resp_test = '''
{"code": 200, "data": {"user": "admin", "select": {"flag": "flag{js0n_n3st}"}}}
'''

def get_nested_flag(test):
    data = json.loads(test)
    return data["data"]["select"]["flag"]
print(get_nested_flag(resp_test))