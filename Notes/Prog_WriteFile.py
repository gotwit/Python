import json

address = {}
address['SriRam'] = {
    "Name":"Ram Mandir",
    "Address":"Ram Janmabhoomi, Sai Nagar, Ayodhya, Uttar Pradesh 224123",
    "Contact":"08009522111"
}

address['SriKrishna'] = {
    "Name":"Shri Vrindavan Chandrodaya Temple",
    "Address":"Vrindavan, Shubham Rd, near Akshaya Patra Temple, Vrindavan, Uttar Pradesh 281121",
    "Contact":"07725977260"
}

s = json.dumps(address)
print(s)
filePath = "C://W//Python//Notes/json_1.txt"
with open(filePath, "w") as f:
    f.writelines(s)
f.close()