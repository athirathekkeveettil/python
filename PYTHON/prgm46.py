# generate a list of four digit numbers in a given range with all their digits eveen and the number is a perfect square

import math
def even(n1,n2):
    l=[]
    if n1>999 and n2<=9999:
         for i in range(n1,n2+1):
             
             
        

def per_squ(n):
   for i in range(l,u):
       if n>=0:
           return int(math.sqrt(n))
        else:
            return 0
        
    

l=int(input("Enter lower limit:"))
u=int(input("Enter upper limit:"))
print("Numbers between",lower,"and",upper,"is",end=" ")
for i in range(lower,upper+1):
    if even(i) and per_squ(i):
        print(i,end=" ")
