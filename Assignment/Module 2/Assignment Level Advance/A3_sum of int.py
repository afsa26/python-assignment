#Write a Python program to sum of three given interers
#however if two values are equal sum will be zero.
a=int(input("Enter the first number:"))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
sum=a+b+c

if (a==b or a==c or b==c ):
    print("sum is zero")

else:
    print("sum is",sum)
