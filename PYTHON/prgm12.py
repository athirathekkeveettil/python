a=input("enter the names:")
a=a.split(",")
print(a)
check = 'b'

b=[i for i in a if i[0].lower()==check.lower()]

print("the list"+str(b))
print(len(b))
