import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore ssl certification errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#read html
url = input('Enter - ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

for i in range(count+1):
    print('Retrieving:', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')


    tags = soup('a')
    if i == count:
        break
    tag = tags[position-1]
    url = tag.get('href', None)
print(url)

#http://py4e-data.dr-chuck.net/known_by_Angus.html