import json

""" 
File open modes

-----------------------------------------------------------------------------
|   r   Opens file for reading only. Throws error if file doesn't exist.    |
|   w   Opens file for writing only. If file doesn't exist then it will     |
|       create new one. If it exist then it will overwrite it.              |
|   r+  Opens file for both reading and writing.                            |
|   w+  Opens file for reading and writing. If file doesn't exist then      |
|       it will create new one. If it exist then it will overwrite it.      |
|   a   Opens a file in append mode. Whatever you wite to file will get     |
|       appended and original content will not be overwritten.              |
|   x   Will create file, returns an error if file doesn't exist.           |
----------------------------------------------------------------------------

"""

filePath = "C://W//Python//Notes/Sample.txt"

""" f=open(filePath, "a")
f.writelines(["Jai Hanuman", "Hari Bol"])
f.close()
 """
with open(filePath, "r") as f:
    data = f.read()
    print(data)

    words = 0
    for line in data.split('\n'):
        tokens = line.split(' ')
        tokenLength = len(tokens)
        words += tokenLength
        print("wordcount: ", len(tokens), "tokens: ", str(tokens))
print("total no of words: ", words)
f.close()

f_in = open("C://W//Python//Notes/Sample.txt", "r")
f_out = open("C://W//Python//Notes/Sample_wc.txt", "w")

for line in f_in:
    tokens = line.split(' ')
    f_out.write("wordcount: " + str(len(tokens)) + " " + line)
f_in.close()
f_out.close()
