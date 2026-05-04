Found = False
print("Before", Found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        Found = True
        print("Found", value)
print("After", Found)