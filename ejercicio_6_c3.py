##In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1736184.json (Sum ends with 39)
#You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.##
import urllib.request, urllib.parse, urllib.error
import ssl
import json
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONEa19
url = input('Enter location - ')
#we do the same until read and after it , we use the decode to traslate the information, just using read i will have a kinda string wit /n, but in byte-string  
html = html = urllib.request.urlopen(url, context=ctx).read().decode()
print('retriving',url)
counter=0
counter2=0

info = json.loads(html)
#important comment must be a string and we have to itterate in info comments, because it is a list in a dictionary
for item in info["comments"]:
    print(item)
    counter+=int(item["count"])

print("count:",len(info["comments"]))   
print("sum",counter)