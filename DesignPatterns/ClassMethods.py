# Type of class creation

# Method 1
class A(object):
    def __init__(self):
        # print("init called to instantiate A")
        pass

a = A()
print()
print(a)

# Method 2
class B(object):
    def __call__(cls, *args, **kwargs):
        # print("call method B")
        return super(B, cls).__call__(cls, *args, **kwargs)

b = B()
print(b)

# Method 3
class C(object):
    def __new__(cls, *args, **kwargs):
        # print("new called")
        return super(C, cls).__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        # print("init called")
        super(C, self).__init__(*args, **kwargs)

c = C()
print(c)

# Method 4
class D(type):
    def __call__(cls, *args, **kwargs):
        return super(D, cls).__call__(*args, **kwargs)

    def __init__(self, name, base, attr):
        super(D, self).__init__(name, base, attr)

class E(metaclass=D):
    pass

e = E()
print(e)

# Method 5
# In python everything is object and class derived from `type`
class F(type):
    def __call__(cls, *args, **kwargs):
        instance = super(F, cls).__call__(*args, **kwargs)
        return instance

    def __init__(self, name, base, attr):
        super(F, self).__init__(name, base, attr)

class G(metaclass=F):
    def __new__(cls, *args, **kwargs):
        return super(G, cls).__new__(cls, *args, **kwargs)
    
    def __init__(self, *args, **kwargs):
        super(G, self).__init__(*args, **kwargs)

g = G()
print(g)


