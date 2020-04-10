def fun(n):
    if n == 0:
        return 1
    else:
        return 7 + fun(n - 2)


print(fun(4))

""" 
    fun(4) = 15
      |
      V
return 7 + fun(2) = 7 + 8 = 15
      |
      V
return 7 + fun(0) = 7 + 1 = 8
      |
      V
reuturn 1
 """
