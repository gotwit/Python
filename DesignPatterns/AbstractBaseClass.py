"""
The statement from __future__ import annotations is used in Python to enable a specific feature that affects type annotations. 
This feature was introduced in Python 3.7 and became the default behavior in Python 3.10.

What It Does
When you import annotations from the __future__ module, it changes the way type hints are evaluated. 
Specifically, it makes type annotations be stored as strings instead of being immediately evaluated. 
This is particularly useful in cases where you want to reference a class or type that hasn't been defined yet 
or when you want to avoid issues with circular imports.

Without from __future__ import annotations, this code would raise a NameError because Node is not yet defined 
at the time it's referenced in the type hint. 
However, with this import, Python treats the type hint Node as a string "Node", which allows forward references and prevents errors.

Why Use It?
Forward References: It allows you to reference a class before it is actually defined.
Improved Performance: Since the annotations are stored as strings, Python doesn't need to evaluate them at runtime, which can lead to faster performance in some cases.
Cleaner Code: It avoids the need for string literals in type annotations, making code cleaner and easier to read.
"""

""" 
Explanation
Automobile(ABC): Automobile is an abstract base class because it inherits from ABC.
@abstractmethod: The sound method is marked as an abstract method. 
This means that any subclass of Automobile must implement the sound method to be instantiated.
Concrete Subclasses (Dog and Cat): These subclasses implement the sound method, so they can be instantiated.
 """

from abc import ABC, abstractmethod

# Automobile inherits Abstract Base Class ABC 
class Automobile(ABC):

    @abstractmethod
    def sound(self):
        pass

    def move(self):
        print("Automobile is moving")

# class Car(Automobile):
#     pass

# class Bike(Automobile):
#     pass

class Car(Automobile):
    def sound(self):
        return "zuiii"

class Bike(Automobile):
    def sound(self):
        return "vroom"

print()
car = Car()
car.move()
print(car.sound())

bike = Bike()
bike.move()
print(bike.sound())

