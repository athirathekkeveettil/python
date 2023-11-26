# Reverse a string

# a)without recursion

s=input("Enter a string:")
r=s[::-1]
print("Reversed string is",r)

# b) with recursion

def str(s):
    if not len(s):
        return " "

    else:
        return s[-1]+str(s[:-1])

s=input("Enter a string:")
print("Reversed string is",str(s))

