a=input("enter the words:")
a=a.split(",")
print(a)
b=int(input("enter a number:"))
print(b)
c=[i for i in a if (len(i)>b)]
print(c)
