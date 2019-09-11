import os
import os.path
from os import path
#import cv2
#import glob
#result_fil='Users\\TOSHIBA\\Desktop\\result.txt'
label="label/"
one=0
two=0
three=0
four=0
five=0
six=0
u=0
files=[]
f = open("resutls.txt")
x = f.readlines()
i=0
j=0
for line in x:
    
    z=line.rstrip()
    y=z.split(",")
    t=y[0].split(".")
    l=t[0]+".txt"
    s=str(t[0])[0]
    #print t
    #print s
    if s==str(1)and y[1]==str(1)and y[4]==str(1) and y[2]==str(0)and y[3]==str(0) and y[6]==str(0)and y[5]==str(0):
        one=one+1
    elif s==str(2)and y[2]==str(1)and y[5]==str(1)and y[1]==str(0)and y[3]==str(0) and y[4]==str(0)and y[6]==str(0):
        two =two+1
    elif s==str(3)and y[2]==str(1)and y[4]==str(1)and y[1]==str(0)and y[3]==str(0) and y[6]==str(0)and y[5]==str(0):
        three =three+1
    elif s==str(4)and y[2]==str(1)and y[6]==str(1)and y[1]==str(0)and y[3]==str(0) and y[4]==str(0)and y[5]==str(0):
        four=four+1
    elif s==str(5)and y[3]==str(1)and y[5]==str(1)and y[2]==str(0)and y[1]==str(0) and y[4]==str(0)and y[6]==str(0):
        five=five+1
    elif s==str(6) and y[3]==str(1)and y[6]==str(1)and y[2]==str(0)and y[1]==str(0) and y[4]==str(0)and y[5]==str(0):
        six=six+1
    
    a=int(y[1])+int(y[2])+int(y[3])+int(y[4])+int(y[5])+int(y[6])
    if a>2:
        j+=1
        #print j,l
    elif a<=1:
        u+=1
        print l
        
    
    
    fil= os.path.join(label,l)
    if path.exists(fil):
        o=open(fil)
        p = o.readline()
        q=p.split(" ")
    
        #print q
        if y[1]==q[0] and y[2]==q[1]and y[3]==q[2] and y[4]==q[3] and y[5]==q[4] and y[6]==q[5]:
            i=i+1
            #print l
            
        
        o.close
    else:
        pass
f.close()
print u
print j
print i
print one
print two
print three
print four
print five
print six
