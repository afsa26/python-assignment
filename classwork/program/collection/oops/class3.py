class Name:
    fname=""
    lname=""
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def MyName(self):
        print("My First Name is :",self.fname)
        print("My last Name is : ",self.lname)

fname=input("Enter your first name: ")
lname=input("Enter your last name :")
a=Name(fname,lname)
a.MyName()