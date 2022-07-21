import os
os.chdir(r'c:/')
if not os.path.exists("newfolder"):
    os.makedirs("newfolder")
else:
    print("Already exists!")