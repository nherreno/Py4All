import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
s=0
url = input('Enter location - ')
#we do the same until read and after it , we use the decode to traslate the information, just using read i will have a kinda string wit /n, but in byte-string  
html = urllib.request.urlopen(url, context=ctx).read().decode()
print('retriving',url)
print('retrivied',len(html))
tree=ET.fromstring(html)
#we use tree.findall , for make a lists of coments
#counts=tree.findall('.//count')
counts=tree.findall('comments/comment')
#'comments/comment' because , we are looking for the complex tag comment in comments
#is a little trick , "To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for any tag named 'count' with the following line of code: (.//count) , idk why but it doesn't run with that line
print(len(counts))
#now is an list with that kinda elements :<Element 'count' at 0x0000020928E06C00> 
lst=[]
for e in counts:
    s += int(e.find('count').text)
print(s)
#the link is http://py4e-data.dr-chuck.net/comments_1736183.xml