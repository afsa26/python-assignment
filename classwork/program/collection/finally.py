x="Tops"
try:
    print(x)
except NameError:
    print("Variable is not defined")

else:
        print("Variable called")
finally:
    print("Finally called")