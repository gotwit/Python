""" 

The statement from __future__ import annotations is used in Python to enable a specific feature that affects type annotations. This feature was introduced in Python 3.7 and became the default behavior in Python 3.10.

When you import annotations from the __future__ module, it changes the way type hints are evaluated. Specifically, it makes type annotations be stored as strings instead of being immediately evaluated. This is particularly useful in cases where you want to reference a class or type that hasn't been defined yet or when you want to avoid issues with circular imports.

Without from __future__ import annotations, this code would raise a NameError because Node is not yet defined at the time it's referenced in the type hint. However, with this import, Python treats the type hint Node as a string "Node", which allows forward references and prevents errors.

Forward References: It allows you to reference a class before it is actually defined.
Improved Performance: Since the annotations are stored as strings, Python doesn't need to evaluate them at runtime, which can lead to faster performance in some cases.
Cleaner Code: It avoids the need for string literals in type annotations, making code cleaner and easier to read.
"""

# Without future import Class reference throws not defined error
from __future__ import annotations

class Node:
    def __init__(self, value: int, next: Node = None):
        self.value = value
        self.next = next
