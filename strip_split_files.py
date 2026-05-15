fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    #print(line)
    if not line.startswith("From: "):
        continue
    words = line.split()
    #print(words)
    words1 = words[1].split('@')
    print(words1[1])