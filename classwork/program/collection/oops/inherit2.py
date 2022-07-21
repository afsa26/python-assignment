class Baseclass():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def test(self):
        print("My first name is",self.fname)
        print("My last name is",self.lname)
class Derivedclass(Baseclass):
    def demo(self):
        print("This is derived class")
a=Baseclass=("Tops","Tech")
b=Derivedclass('Tops','Tech')
b.test()
b.demo()