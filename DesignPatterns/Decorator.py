class Decorator(object):

    # class variable
    var1 = 3

    def __init__(self, num=1):
        self.num = num
        # _ (1d single underscore) variable in the beginning is for non private
        # __ (dund double underscore) for private variable
        self._num1 = 2
        self.__num2 = 3
        # pass

    def getter(self):
        return self.__num2

    def setter(self, val):
        self.__num2 = val

    # without property decorator
    def whatsup(self):
        print("whatsup")

    @property
    def pookie(self):
        print("pookie")

    @property
    def gucci(self):
        strng = "gucci"
        return strng

    # static methods dont have self param, explicity annotation is required
    @staticmethod
    def goat():
        print("Python is goat")

    def sick():
        print("can't stop programming python")

    def __str__(self):
        return "object test"

    
    def getClassVariable(cls):
        print("class variable access {}".format(cls.var1))

if __name__ == "__main__":
    obj = Decorator()
    print(obj)
    print(obj.num)
    print(obj._num1)
    # AttributeError: 'Decorator' object has no attribute '__num2'
    # print(obj.__num2)

    # prints the value of private variable by using getter and setter
    print(obj.getter())

    # set the value of a private variable and print
    obj.setter(369)
    print(obj.getter())

    # without property decorator use () brackets and return None because using print method
    print(obj.whatsup())
    obj.whatsup()

    # with property decorator dont use () brackets, throws error if () are and return None
    # because print method is used
    print(obj.pookie)
    obj.pookie

    print(obj.gucci)

    # static method requires () brackets
    obj.goat()

    Decorator.goat()

    # using class name to refer instance method
    Decorator.sick()

    # TypeError: Decorator.sick() takes 0 positional arguments but 1 was given
    # means this / self parameter is passed as an argument if not explicity specified as static
    # obj.sick()

    print(obj.getClassVariable())
