import json

json_name = "sample-1.json"
name = json_name.rstrip(".json")
print(name)

with open(json_name, "r") as j:
    json_data = json.load(j)


print(json_data.values())
