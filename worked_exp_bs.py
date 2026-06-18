# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl

# #ignore ssl certification errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# #read html
# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')

# tags = soup('a')
# for tag in tags: 
#     print(tag.get('href',None))

print(chr(42))
print(chr(108), chr(105), chr(110), chr(101))