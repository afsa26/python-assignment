#Write a Python program to find the first appearance of the substring 'not'
#and 'poor' from a given string,if 'not'follows the'poor',replace the whole
#'not'...'poor'substring with'good'.return the resulting string.
def longlength(a):
    max1=len(a[0])
    temp=a[0]

    for i in a:
        if(len(i)>max1):
            max1=len(i)
            temp=i
    print("The word with the longest length is:",temp,"and length is",max1)
    a=["one","two","three","four"]
    longlength(a)