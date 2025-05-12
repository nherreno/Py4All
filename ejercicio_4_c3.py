#In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count=int(input("count:"))
position=int(input("position:"))
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
print("retrieving:",url)
# Retrieve all of the anchor tags
tags = soup('a')

for i in range(count):
    link=tags[position-1].get('href', None)
    # we use postion-1 for just take one of the lines not all , like a list 
    print("retrieving",link)
    #we obtain the first link
    html = urllib.request.urlopen(link, context=ctx).read()
    #we read the new link
    soup = BeautifulSoup(html, 'html.parser')
    #we use soup for organize the link 
    tags = soup('a')
    #we change the value and do it in a loop, in range of the count-1

#link http://py4e-data.dr-chuck.net/known_by_Cameron.html 7times position 18 response is Amieleigh