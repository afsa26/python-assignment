class person:
    def FullName(self,fname,lname):
        print(fname,lname)

class Customer(person):
    def FullName(self,fname,lname,age):
        print(fname,lname,age)
obj2=Customer()
#obj.FullName("tops","tech",12)
obj2=person()
obj2.FullName("demo","demo")