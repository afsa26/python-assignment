B1.What is the python.what is Python.Name some features of Python.
A1.Python is an interpreted object oriented ,high level programming
   language with dynamic semantics.Python's simple,			
   easy to learn syntax emphasizes readability therefore
   reduces the cost of program maintenance.Python supports modules
   and packages,which encourages program modularity and code reuse.
   Features of python:
      ->clean syntax plus high level data types
      ->uses white space to delimit blocks
      ->variables do not need declaration

B2.write a python program to get the python version you are using?
A2. 
import sys
print("Python Version")
print(sys.version)
print("Version Info")
print(sys.version_info)

B3.Is Python right choice for web based programming?
A3.The language of python is extreamly powerful and very advanced
over other for web design and development Python programming yields an advantage over other programming languages when it comes to highly functional programming.
which is a must have for websites and applications.

B4.Why was the language called as python?
A4.When he began implementing Python, Guido van Rossum was also 
reading the published scripts from “Monty Python's Flying Circus”,
a BBC comedy series from the 1970s. Van Rossum thought he needed a 
name that was short, unique, and slightly mysterious, so he decided
 to call the language Python.

B5.Write a Python program to check If a number is positive,nagative or zero.

A5.
number =float(input("Enter no:"))

if number>0:
   	 	 print ("Number is positive")

elif number==0 : 	
   		 print("Number is Zero")

else:
    		 print("Number is Nagative")
nested if:
number=float(input("Enter no:"))

if number>=0:
    	if number==0:
     			print("Number is Zero")
        else:
      			print("Number is Positive")
else:
    		    print("Number is Nagative")
B6.What is the language from which python has got its features or
 derived its features?
A6.Python is derived from programming languages such as ABC,
   Modula 3, small talk, Algol-68. Van Rossum picked the name
   Python for the new language from a TV show, Monty Python's 
   Flying Circus.
B7.Write a program to check if variable is integer or string.
A7.
str=(input("Enter Value: "))

if str.isdigit():

   			print("Variable is Integer")

else:
    		print("variable is String")

B8.Does Python support switch or case statement in Python?
If not what is the reason for the same?
A8.Python does not support switch or case statement.because 
of Unsatisfactory Proposals Most programming languages have 
switch/case because they don't have proper mapping constructs. 
You cannot map a value to a function, that's why they have it.

B9.How python is interpreted?
A9.Python is an interpreted language, which means the source code
   of a Python program is convertedinto bytecode that is then executed
   by the Python virtual machine. Python is different from major 
   compiled languages, such as C and C + +, as Python code is not
   required to be built and linked like code for these languages.

B10.Write a Python program to get the Factorial number of given number.
B10.

B11.Write a Python program to get the Fibonacci series of given range.
A11.	num=int(input("enter the given num: "))
a=1
b=0
print(b)
print(a)
for i in rasnge(1,10):
 c=b
 b=a
 a=c + b
 print(a)

B12.How memory is managed in Python?
A12.Memory management in Python involves a private heap containing
all Python objects and data structures. On top of the raw memory
allocator, several object-specific allocators operate on the same 
heap and implement distinct memory management policies adapted to
the peculiarities of every object type.



B13.What is the namespace in Python?
A13.A namespace is a system that has a unique name for each and 
every object in Python.sAn object might be a variable or a method.
 Python itself maintains a namespace in the form of a Python dictionary.


B14.What is the purpose continue statement in Python?



























