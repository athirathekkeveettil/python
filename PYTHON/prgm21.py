

b=input("enter the sentence:")
b=b.split(" ,")
print(str(b))
a={}
for i in b:
    a[i]=a.get(i,0)+1
print(a)
