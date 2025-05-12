#Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
count=0
lst=[]
fh = open(fname)
for line in fh:
    line=line.strip()
    word=line.split()
    if len(word)<1:
        continue
    if word[0]=="From" and not word[0]=="From:":
        print(word[1])
        count+=1
    #if line.startswith("From") and not line.startswith("From:") :
        #lst1=line.split()
        #count=count+1
        #print(lst1[1])#this gives us the same reponse
#if line.startswith("From"):
#lst1=line.split()
#if len(lst1)>2:
#count=count+1
#print(lst1[1])
#this codes , give us the same reponse for the example
print("There were", count, "lines in the file with From as the first word")
            
    