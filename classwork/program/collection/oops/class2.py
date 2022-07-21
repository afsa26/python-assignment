class Myclass:
    x=0
    def __init__(self,x):
         self.x = x

    def OddEven(self):
        if self.x%2==0:

            print(x,"is Even Number")

        else:
            print(x,"is Odd Number")
x=int(input("Please Enter a Value:"))
a=Myclass(x)
a.OddEven()