import json

filePath = "C://W//Python//Notes/json_1.txt"

f=open(filePath, "r")
s=f.read()
print(type(s),s)
f.close()
address=json.loads(s)
print("address count: ", len(address), type(address), address)
print(address['SriKrishna'])
print(address['SriKrishna']['Contact'])

for addr in address:
    print(address[addr])

 