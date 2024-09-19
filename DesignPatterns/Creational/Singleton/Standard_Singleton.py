
""" 
Singleton
It is a creational design pattern, which ensures that only one object of class exists and
provides a single point of access to it.
"""

"""
Singleton can be implemented in different ways. Some possible methods include:
base class, decorator, metaclass.
"""

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of `__init__` argument do not affect the returned instance.
        If instance already exists do not create
        """
        if cls not in cls._instances:
            instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    # value: str = None

    def __init__(self):
        print("Singleton init call")
    
    # def __init__(self, value: str=""):
    #     self.value = value
    #     print("Singleton init call")

    def __init__(self, *args):
        if len(args) == 1:
            self.value = args[0]
        # elif len(args) == 2:
        #     self.value = args[0] + args[1]
        else:
            self.value = None

    def business_logic(self):
        print("business logic is here")
        

# if __name__ == "__main__":
#     s1 = Singleton()
#     s2 = Singleton()

#     if id(s1) == id(s2):
#         print("Singleton works, variables contain same instace.")
#     else:
#         print("Singleton failed, variables contain different instances.")


# obj1 = Singleton()
# print(obj1)

# obj2 = Singleton()
# print(obj2)

obj3 = Singleton("First instance")
print(obj3)
print(obj3.value)

obj4 = Singleton("Second instance")
print(obj4)
print(obj4.value)