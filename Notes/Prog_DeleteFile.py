import os

filePath = "C://W//Python//Notes/Sample_del.txt"

if not os.path.exists(filePath):
    f=open(filePath, "x")
    f.close()
    print(f.closed)
os.remove(filePath)

if os.path.exists(filePath):
    print("file exists")
else:
    print("file doesn't exist")

