fh = open('mbox-short.txt')
count = 0
for line in fh:
    line = line.strip()
    wds = line.split()

    if len(wds) < 3:
        continue
    if wds[0] != 'From':
        continue 
    print(wds[1])
    count += 1
print("there are {} emails".format(count))