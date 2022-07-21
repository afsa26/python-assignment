#Write a Python program that accepts an integer(n)and coputes the value of
#n+nn+nnn
#a=int(input("Enter the value : "))
#n1=("%s"%a)
#n2=("%s%s"%(a,a))
#n3=("%s%s%s"%(a,a,a))
#print(n1+n2+n3)

#metod 2
n=int(input("Enter a number n :"))
temp=str(n)
t1=temp+temp
t2=temp+temp+temp
cmpt=n+int(t1)+int(t2)
print("The value is",cmpt)
