name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
d = dict()
handle = open(name)
for line in handle:
    line = line.strip()
    wds = line.split()
    if len(wds) < 3 or wds[0] != 'From':
        continue
    else:
        email = wds[1]
        d[email] = d.get(email,0) + 1


emailcount = None
freqemail = None
for email,counts in d.items():
    if emailcount is None or counts > emailcount:
        freqemail = email
        emailcount = counts
print(freqemail, emailcount)