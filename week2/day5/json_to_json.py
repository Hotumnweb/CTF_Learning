import json

def to_json(d):
    return json.dumps(d, ensure_ascii=False, indent=2)

print(to_json({"用户名": "admin", "权限": ["读", "写"]}))