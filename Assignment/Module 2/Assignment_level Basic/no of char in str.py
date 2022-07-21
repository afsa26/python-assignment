#Write a Python Program to count the number of characters(char frequency)in string
string=input("Enter the string: ")
char=input("Please Enter the char to find frequency of character\n")

count=0
for i in range(len(string)):
    if(string[i]==char):
        count=count+1
print("The frequency of the ",char,"in the string is:",count)