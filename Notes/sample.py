file = open(r"C:\W\Python\Notes\sample.txt", "r+")
print(file.readline())
file.writelines("Jai Sri Ram")
print(file.readline())