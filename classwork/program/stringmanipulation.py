str="tops technologies"
#print(str.capitalize())
#print (str.casefold())
#print (str.center(70))
#print(str.count('o'))
#print(str.endswith("es"))
#print(str.startswith("to"))
#print(str.find("ch"))
#print(str.index('ps'))

a="Tops123"
print(a.isalnum())
b="tops"
print(b.isalpha())
c='147'
print(c.isdigit())
print(b.isidentifier())
print(b.islower())
d="Hello"
print(d.istitle())
e="WORLD"
print(e.isupper())
print("-".join(d))
print(str.ljust(50,'*'))
print(str.partition('t'))
print(e.replace('D','O'))
print(str.split('o'))
print(e[2])
print(e[1:5])
i="Hello Python!"
print(i[6:12])
print(i[-6:-3])
