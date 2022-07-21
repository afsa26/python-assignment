#global variable
from unicodedata import name


a="Tops tech"
b="Hello world"

#def test(a):
#    print(a)
#print("demo")
#print(a)

def test():
     global name
print("1st",name)
name="Python progrmming"
print("2nd",name)

name="php programming"
test()
#local variable
def demo():
    a="test"
    print(a)
demo()