name = input("what is your name")
people = [{"name": "Victoria", "age": 43}, {"name":"joy", "age":32}, {"name": "Blessing", "age": 44}]
for i in people:
    if name == i["name"]:
        print(f"hello, your name is {i}")
    