a=input("Enter the numbers:")
a=list(map(int,a.split(",")))
print(a)
b=[i for i in a if(i>0)]
print(b)
