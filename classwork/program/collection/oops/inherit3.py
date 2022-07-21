class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        print(self.x*self.y)

class B(A):
    def test(self):
        print("This is b class")
class C(B):
    def demo(self):
        print("This is c class")
obj=C(2,3)
obj.add()
obj.test()
obj.demo()
