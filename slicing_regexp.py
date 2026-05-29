import re
from_string = "From stephan.marqared@uct.ac.za sat Jan 5 09:14:16 2008"

# atpos = from_string.find('@')
# print(atpos)
# sppos = from_string.find(' ', atpos)
# print(sppos)
# host = from_string[atpos+1 : sppos]
# print(host)

#lin = re.findall('@([^ ]*)', from_string)
#print(lin)

lin1 = re.findall('^From  .*@([^ ]*)', from_string)
print(lin1)