class Myclass:
    a=12
    print(a)
    def test(x):
        print("test function")
        print(x)
    def __init__(self,y):
        print("init method")
        print(y)

Myclass("This is y value")
Myclass.test("Tops")