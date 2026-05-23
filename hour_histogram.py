name = input("Enter file:")
d = dict()
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if not line.startswith("From "):
        continue
    line = line.strip()
    line = line.split()
    time = sorted(line)[0]
    hr = time.split(":")[0]
    d[hr] = d.get(hr,0) + 1

l = sorted([(k,v)for k,v in d.items()])
for k,v in l:
    print(k, v)