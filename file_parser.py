fname = input("enter the file: ")
if len(fname) < 1: 
    fname = "clown.txt"
fhand = open(fname)
many = dict()

for line in fhand:
    line = line.strip()
    wds = line.split()
    print(wds)
    for w in wds:
        #print("=============>", w)
        #print(w)
        #print(many)
        # oldvalue = 0
        # if w in many:
        #     oldvalue = many[w]
        #oldvalue = many.get(w,0)
        #rint("oldvalue",oldvalue)
        many[w] = many.get(w,0) + 1

for k, v in many.items():
    print(k, v)

#word  with greatest count
largest = None
for k, v in many.items():
    if largest is None or v > largest:
        largest = v
        word = k
print("the most common word is:", word)
print("the count is:", largest)