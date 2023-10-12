a=int(input('enter year:'))
print(a)
b=[i for i in range(2023,a) if (i%4==0)and(i%100!=0)or(i%400==0)]
print(b)
