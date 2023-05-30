name = []
for i in range(10):
    names = (input("enter a name"))
    if len(name) > 11:
        break
    else:
        name.insert(i, names)
print(name)
