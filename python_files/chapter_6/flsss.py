import json

records = {"student_records": [
    {"id": 1, "name": "ebuka", "age": 41},
    {"id": 2, "name": "eddie", "age": 53},
    {"id": 3, "name": "aphia", "age": 32},
]}

with open("records.json", mode='w') as rec:
    json.dump(records, rec)

with open("records.json", mode='r') as rec2:
    print(json.dumps(json.load(rec2), indent=4))