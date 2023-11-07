# generate a string by combining 1st 2 characters and last 2 characters from an input string.If length of input strings is 2,then resultant string must be a concatenation of those characters or if length is less than than 2,return an empty string instead

a=input("Enter a string:");
if len(a)==2:
    b=a*2
elif len(a)>2:
    b=a[:2]+a[-2:]
    print(b)
else:
    print("Empty")
    
