class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minMaxStack = []

    def peek(self):
        return self.stack[len(self.stack)-1] if len(self.stack)-1 >= 0 else "Empty stack"

    def push(self, number):
        minMaxItem = {"min": number, "max": number}
        if len(self.minMaxStack):
            lastMinMaxItem = self.minMaxStack[len(self.minMaxStack) - 1]
            minMaxItem["min"] = min(number, lastMinMaxItem["min"])
            minMaxItem["max"] = max(number, lastMinMaxItem["max"])
        self.minMaxStack.append(minMaxItem)
        self.stack.append(number)

    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack)-1]["min"] if len(self.minMaxStack)-1 >= 0 else "Empty stack"

    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["max"] if len(self.minMaxStack)-1 >= 0 else "Empty stack"


if __name__ == "__main__":
    minMaxStack = MinMaxStack()
    print(f"push 5: {minMaxStack.push(5)}")
    print(f"getMin: {minMaxStack.getMin()}")
    print(f"getMax: {minMaxStack.getMax()}")
    print(f"peek: {minMaxStack.peek()}")
    print(f"push 7: {minMaxStack.push(7)}")
    print(f"getMin: {minMaxStack.getMin()}")
    print(f"getMax: {minMaxStack.getMax()}")
    print(f"peek: {minMaxStack.peek()}")
    print(f"push 2: {minMaxStack.push(2)}")
    print(f"getMin: {minMaxStack.getMin()}")
    print(f"getMax: {minMaxStack.getMax()}")
    print(f"peek: {minMaxStack.peek()}")
    print(f"push: {minMaxStack.push(9)}")
    print(f"getMin: {minMaxStack.getMin()}")
    print(f"getMax: {minMaxStack.getMax()}")
    print(f"peek: {minMaxStack.peek()}")
    print(f"pop: {minMaxStack.pop()}")
    print(f"getMin: {minMaxStack.getMin()}")
    print(f"getMax: {minMaxStack.getMax()}")
    print(f"peek: {minMaxStack.peek()}")
    print(f"pop: {minMaxStack.pop()}")
    print(f"getMin: {minMaxStack.getMin()}")
    print(f"getMax: {minMaxStack.getMax()}")
    print(f"peek: {minMaxStack.peek()}")
    print(f"pop: {minMaxStack.pop()}")
    print(f"getMin: {minMaxStack.getMin()}")
    print(f"getMax: {minMaxStack.getMax()}")
    print(f"peek: {minMaxStack.peek()}")
    print(f"pop: {minMaxStack.pop()}")
    print(f"getMin: {minMaxStack.getMin()}")
    print(f"getMax: {minMaxStack.getMax()}")
    print(f"peek: {minMaxStack.peek()}")
