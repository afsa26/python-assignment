fruits=["Apple","orange","Kiwi","Mango",123,4567]
#print (fruits)
#print(type(fruits))
print(fruits[2])
print(fruits[1:3])
print (fruits[-6:-3])
for fruits in "orange":
    print(fruits,end=" ")
data=[12,45,60,80]
print (data)
print(len(data))
print(max(data))
print(min(data))

var=["hello","Good","day"]
print(type(var))
print(list(var))

data.append("Hello")
#print (data)
#data.extend("hello")
data.insert(2,"hello")
print(data)
print(data.count(80))
print (data.index(60))
data.pop()
data.reverse()
print(data)

i=["php","java","python","asp"]
i.sort()
i.remove("java")
print (i)

i.append("Html")
#i.pop()
print(i)

if "python" in i:
    print("yes,its found")

else:
     print("not found")

if "python" not in i:
    print("not found")
else:
    print("found")

d=[]
for y in range(10):
     d.append(y**2)
     print(d)

for i in range(6,0):
   print("*"*i)

    
    