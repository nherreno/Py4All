# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
mail=dict()
lista=list()
count=0
for line in handle:
    words=line.split()
    if len(words)>2 and words[0]=="From":
        lista.append(words[1])

for word in lista:
    mail[word]=mail.get(word,0)+1

 
    
grande=None
palabra=None

for a,b in mail.items():
    if grande==None or b>grande:
        grande=b
        palabra=a
        
print(palabra,grande)

#otra manera de hacerlo 
#fname = input("Enter file:")
#if len(fname) < 1 : name = "mbox-short.txt"
#hand = open(fname)

#lst = list()

#for line in hand:
    #if not line.startswith("From:"): continue
    #line = line.split()
    #lst.append(line[1])

#counts = dict()
#for word in lst:
    #counts[word] = counts.get(word,0) + 1

#bigcount = None
#bigword = None
#for word,count in counts.items(): 
    #if bigcount is None or count > bigcount:
        #bigcount = count
        #bigword = word

#print (bigword,bigcount)