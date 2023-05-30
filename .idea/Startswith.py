found = False
names = [ 'david', 'mariam', 'lateef', 'sali']
for name in names:
    if name.startswith("J"):
        print("found")
        found = True
    # if not found:      (ANOTHER METHOD)
    #     print("not found")
    else:
        print("not found")