def numbering():
    lis1 = ["female", "male", "Female", "Male", "male"]
    lis2 = [lis1[0], lis1[1], lis1[2].lower(), lis1[3].lower(), lis1[4]]
    print(lis2)
    lis3 = [lis2[0], lis2.count(lis1[0]), lis2[1], lis2.count(lis1[1])]
    print(lis3)
numbering()
