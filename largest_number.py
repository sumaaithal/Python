largest_so_far = -1
for i in [9, 41, 12, 3, 74, 15]:
    if i > largest_so_far:
        largest_so_far = i 
    print("largest so far", largest_so_far, "and i is", i)
print("After", largest_so_far)