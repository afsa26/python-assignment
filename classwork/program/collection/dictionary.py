var={'name':"tops",'age':12,'place':"ahmedabad"}
# print(var)
print(var['name'],var['age'],var['place'])
# IT={"frontend":("wd","react","angular"),"Backend":("php","python")}
#IT={"frontend":["wd","react","angular"],"Backend":["php","python"]}
#print(IT['frontend'])
city={'name':'ahemedabad','area':'cgroad','age':52}
var.update(city)
#print(var)
#print(city.values())
#print(city.keys())
#print(city.items())
#print(city.clear())
for x in city:
    print(x,city[x])

a={"id":11,"name":"afsana","age":30,"salary":50000}
for b in a:
    print(b,"^",a[b])

