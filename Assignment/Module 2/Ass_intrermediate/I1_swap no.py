#write a Python Program that swap two number with temp variable
#  and without temp variable.
#using temp variable
a=10
b=7
temp=a
a=b
b=temp
print(a)
print(b)

#without using temp variable.

a=5
b=9
a,b=b,a
print(a)
print(b)
