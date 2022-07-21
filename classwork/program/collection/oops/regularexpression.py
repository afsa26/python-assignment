import re
if (re.search("Python","Python is programming language")):
    print("match found")
else:
    print("match is not found")

x="Python latest version is v3.10"
print(re.findall(r'^\w+',x))
print(re.split('r\s',x))

print(re.match(r'python',"python php java"))
word="dog,bot,god,rose,not"
regex=re.compile("bot")
word=regex.sub("Tops",word)
print(word)

name="Python is world's best programming language"
for i in re.finditer("is",name):
    ans=i.span()
    print(ans)