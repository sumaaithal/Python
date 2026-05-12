inp = input("enter the file name:")
try:
    fhand = open(inp)
    for line in fhand:
        line = line.rstrip()
        print(line.lower())
except:
    print("file cannot be opened:", inp)
    exit()

