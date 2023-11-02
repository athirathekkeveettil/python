# print out all colors from a color list 1 not contained in color list 2

a=input("enter color-list 1:")
a=a.split(",")
b=input("enter color-list 2:")
b=b.split(",")

print(set(a)-set(b))

