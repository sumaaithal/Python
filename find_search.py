#find like search
# find 

# handle = open('mbox-short.txt')
# for line in handle:
#     line = line.rstrip()
#     if line.find('From:') >= 0:
#         print(line)

# re.search 

# import re 

# handle = open('mbox-short.txt')
# for line in handle:
#     line = line.rstrip()
#     if re.search('From:', line):
#         print(line)

#search like startswith
#startswith

# handle = open('mbox-short.txt')
# for line in handle:
#     line = line.rstrip()
#     if line.startswith('From:'):
#         print(line)

#search

import re
handle = open('mbox-short.txt')
for line in handle:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
