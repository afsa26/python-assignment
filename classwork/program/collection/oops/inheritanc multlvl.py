class A:
        def __init__(self,name,age):
            self.name=name
            self.age=age

        def test(self):
            print("name is",self.name)
            print("age is",self.age)
class B(A):
        def demo(self):
            print("This is b class")
class C(A):
    def MyDef(self):
        print("This is c class")
obj= C("Tops",12)
obj.test()
obj.MyDef()

obj2=B("Hello",11)
obj.test()
obj.demo()