a=input("enter the numbes:")
a=list(map(int,a.split(",")))
print(a)
b=[i for i in a if (i%2!=0)]
print(b)
