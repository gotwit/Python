"""
 Stack operations

1. push() / insert() to insert an element into the Stack
2. pop() / remove() to remove an element from the Stack
3. top() / peek() to return an element from the stack_data
4. isEmpty() returns True if stack is empty else False
5. isFull() returns True if stack is full else False
 """

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:


    def __init__(self):
        self.root = None
        self.inf = float("-inf")

    
    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.root
        self.root = newNode
        return newNode.data

    
    def pop(self):
        if self.root is None:
            return self.inf
        node = self.root
        data = node.data
        self.root = self.root.next
        return data


    def peek(self):
        if self.root is None:
            return self.inf
        return self.root.data


    def isEmpty(self):
        return True if self.root is None else False


stk = Stack()

n = int(input("Enter the number of iterations: "))

while n > 0:
    try:
        status = int(input("""
    Enter 0 to print stack
    Enter 1 to push
    Enter 2 to pop
    Enter 3 to peek
    Enter 4 to check stack is empty
    Enter -1 to exit
    """))

        match status:
            case -1:
                print("exited")
                break
            case 0:
                node = stk.root
                while node is not None:
                    print(node.data, end=" ")
                    node = node.next
            case 1:
                data = int(input("Enter a value: "))
                stk.push(data)
                print(data, "pushed to stack")
            case 2:
                item = stk.pop()

                if item is not stk.inf:
                    print(item, "popped from stack")
                else:
                    print("Stack has no elements to remove")
            case 3:
                item = stk.peek()

                if item is not stk.inf:
                    print("Peek value: ", item)
                else:
                    print("Stack has no elements to show")
            case 4:
                isEmpty = stk.isEmpty()
                print("Stack is empty" if isEmpty else "Stack is not empty")
            case _:
                print("Please enter valid choice")


        n -= 1
    except ValueError:
        print("Please enter valid choice")