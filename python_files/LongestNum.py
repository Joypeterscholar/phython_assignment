name = ["joy", "david", "joy", "stella", "joy"]
max = name[0]
for i in range(len(name)):
    if name[i] >= max:
        max = name[i]
result = (max, len(max))
print(result)
