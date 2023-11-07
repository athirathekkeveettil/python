# write a function that accepts full name and display in reverse order of words with space between them  


def reverse(a):
    for word in a[::-1]:
        print(word,end=" ")


a=input("enter Full Name:")
a=a.split(" ")
reverse(a)
