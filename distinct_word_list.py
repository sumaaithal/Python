fh = open('romeo.txt')
lst = []
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
            lst.sort()
print(lst)