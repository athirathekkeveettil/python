# accept percentage of marks from user and display the grade

a=float(input("enter the percentage of mark:"))
if (a>=95):print("Grade:S")
elif (a>=90):print("Grade:A+")
elif (a>=80):print("Grade:A")
elif (a>=70):print("Grade:B+")
elif (a>=60):print("Grade:B")
elif (a>=50):print("Grade:C+")
elif (a>=40):print("Grade:C")
else:
    print("YOU ARE FAILED")
