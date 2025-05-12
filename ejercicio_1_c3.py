#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers. regex sum 42 is the example 

import re
#handle=open("regex_sum_42.txt")
#handle=open("regex_sum_1736179.txt")
#count=0

#for line in handle:
    #ls=re.findall("[0-9]+",line) 
    #if len(ls)<1:
        #continue
    #for i in ls:
        #count=count+float(i)
#print(int(count))
print( sum( [int(i) for i in re.findall('[0-9]+',open("regex_sum_1736179.txt").read()) ] ) )
    
    
    