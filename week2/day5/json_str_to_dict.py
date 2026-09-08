import json

def parse_json(test):
    data = json.loads(test)
    return data["name"], data["tags"][0]

s = '{"name": "admin", "tags": ["web", "crypto"]}'
print(parse_json(s))