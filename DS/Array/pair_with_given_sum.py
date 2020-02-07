arr = [8, 7, 2, 5, 3, 1]
sum = 10
dict = {}

# O(n) time
for i in arr:
    try:
        dict[sum - i]
        print(i, sum - i)
    except:
        # dict[i] = "" dictionary will be incomplete here
        pass
    dict[i] = ""
print(dict)
