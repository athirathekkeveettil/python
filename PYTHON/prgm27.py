#print out all colors from color list 1 not contained in color list 2
a=input("Enter the colors in 1:")
a=a.split(",")
b=input("Enter the colors in 2:")
b=b.split(",")
print("The colors:",set(a)-set(b))
