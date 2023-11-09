# List comprehensions:
# a)Generate positive list of numbers from a given list of numbers

a=input("Enter the numbers:")
a=list(map(int,a.split(",")))
print(a)
b=[i for i in a if(i>0)]
print(b)

# b)Generate a list with square of numbers from a given list

a=input("Enter the numbers:")
a=list(map(int,a.split(",")))
print(a)
b=[i*i for i in a]
print(b)


# c)Form a list containing vowels from a given word

a=input("Enter the word:")
b=[i for i in a if i in "aeiouAEIOU"]
print(b)


# d)Generate a list of numbers by removing even numbers from a given list

a=input("enter the numbers:")
a=list(map(int,a.split(",")))
print(a)
b=[i for i in a if (i%2!=0)]
print(b)

# e)Display leap year from current year to a future year entered by user

a=int(input('enter year:'))
print(a)
b=[i for i in range(2023,a) if (i%4==0)and(i%100!=0)or(i%400==0)]
print(b)
