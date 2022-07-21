#Write a Python program to count the occurences of each word in a given sentence.
string="This is a sample of Python program, Welcome to world of python programming"
word="Python"
list=[]
wordcount=0
list=string.split(" ")
for i in range(0,len(list)):
    if(word==list[i]):
        wordcount=wordcount+1
print("Number of occurences found in the string:")
print(wordcount)