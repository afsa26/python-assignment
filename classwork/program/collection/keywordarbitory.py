#def name(**age):
 #   print(age)

#name()
#name(ty=12,fname=45,lname="dh")


def name(**all):
    for key,value in all.items():
        print(key,value)
name(fname="john",lname="doe")