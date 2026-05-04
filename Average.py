Count = 0
Sum = 0
print("Before", Count, Sum)
for num in [9, 41, 12, 3, 74, 15]:
    Count = Count + 1 #counting the number of items in the list
    Sum = Sum + num #runing total of the sum
    print(Count, Sum, num)
print("After", Count, Sum, Sum/Count)