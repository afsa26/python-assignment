a=int(input("Enter the first value:"))
b=int(input("Enter the second value:"))

try:

    c=a+b
    print(a,"+",b,"=",c)
except Exception:
    print("Exception caught")
finally:
     print("Finally called")
    #print("Exception completed")
