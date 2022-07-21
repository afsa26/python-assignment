#Write a Python program to get a single string from two given strings.
#seprater by space and swap the first two character of each string.
str1=input("Enter the First string:")
str2=input("Enter the Second string: ")
#x=str1[0:2]
str1=str1.replace(str1[0:2],str2[0:2])
#str2=str2.replace(str2[0:2],x)
print("Your First string is Become ",str1)
