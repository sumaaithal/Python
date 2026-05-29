import re 
string = "These are my favorite numbers: 4, 8, 15, 16, 23, and 42"

numbers = re.findall('[0-9]+', string)
print(numbers)

chars = re.findall('[AEIOU]+', string)
print(chars)

f = 'From: Using the : character'
x = re.findall('^F.+:', f)
print(x)

x = re.findall('^F.+?:', f)
print(x)

from_string = "From: xyz@uct.com sat Jan 5 09:14:16 2008"
email = re.findall('\S+@\S+', from_string)
print(email)

from_string1 = "From: xyz@uct.com sat Jan 5 09:14:16 2008"
email1 = re.findall('^From: (\S+@\S+)', from_string1)
print(email1)