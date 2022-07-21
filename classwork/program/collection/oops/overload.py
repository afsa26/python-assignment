class Myclass:
    def __init__(self,a):
        self.a=a
    def __add__(self,b):
        return self.a+b.a
obj=Myclass(2)
obj2=Myclass(5)
print(obj+obj2)

x=Myclass("Python")
y=Myclass("Programming")
print(x+y)