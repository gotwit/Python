"""
 Stack operations

1. push() / insert() to insert an element into the Stack
2. pop() / remove() to remove an element from the Stack
3. top() / peek() to return an element from the stack_data
4. isEmpty() returns True if stack is empty else False
5. isFull() returns True if stack is full else False
 """


class Stack:

    
    def __init__(self, capacity=0):
        self.lst = []
        self.capacity = capacity
        self.top = -1


    def push(self, value):
        if self.capacity != (self.top + 1):
            self.lst.append(value)
            self.top = self.top + 1
            return self.lst
        else:
            return None


    def pop(self):
        if self.top != -1:
            item = self.lst.pop()
            self.top = self.top - 1
            return item
        else:
            return None


    # def top(self):
    #     if self.top != -1:
    #         index = self.top
    #         return self.lst[index]
    #     else:
    #         return None


    def peek(self):
        if self.top != -1:
            index = self.top
            return self.lst[index]
        else:
            return None


    def isEmpty(self) -> bool:
        return self.top == -1


    def isFull(self) -> bool:
        return self.capacity == (self.top + 1)


    def show(self):
        return self.lst


size = int(input("Enter the size of stack: "))
stk = Stack(size)

# print("Size of stack: ", stk.capacity)

n = int(input("Enter the number of iterations: "))

while n > 0:
    status = int(input("""
Enter 0 to print stack
Enter 1 to push
Enter 2 to pop
Enter 3 to peek
Enter 4 to check stack is empty
Enter 5 to check stack is full
"""))

    match status:
        case 0:
            print("Stack :", stk.show())
        case 1:
            value = int(input("Enter a value: "))
            lst = stk.push(value)
            if lst is not None:
                print(lst)
            else:
                print("Stack size is incorrect")
        case 2:
            item = stk.pop()
            if item is not None:
                print("Removed ", item)
            else:
                print("Stack has no elements to remove")
        case 3:
            item = stk.peek()
            if item is not None:
                print("Peek ", item)
            else:
                print("Stack has no elements to show")
        case 4:
            isEmpty = stk.isEmpty()
            print("Stack is empty" if isEmpty else "Stack is not empty")
        case 5:
            isFull = stk.isFull()
            print("Stack is full" if isFull else "Stack is not full")

    n -= 1
