# evaluate conditional statements

# a)check whether a given number is even or odd and return 'EVEN' or 'ODD' appropriately

a=int(input("Enter a number:"))
print("EVEN" if not a%2 else "ODD")

# b)check whether an item is available in a list and return 'AVAILABLE' or 'NOT AVAILABLE' appropriately

a=input("Enter alist of items:")
a=a.split(",")
item=input("Enter the item to check:")
print("AVAILABLE" if item.lower() in a else "NOT AVAILABLE")
