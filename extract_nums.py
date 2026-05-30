import re 

num_list = []
tot = 0
h = open('textt_sum.txt','r')
strings_list = h.readlines()
for line in strings_list:
    lin = line.strip()
    y = re.findall('[0-9]+', lin)
    if len(y) < 1:
        continue
    num_list.extend(y)

for num in num_list:
    tot = tot + int(num)
print(tot)