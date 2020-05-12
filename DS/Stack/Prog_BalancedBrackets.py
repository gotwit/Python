# O(n) time | O(n) space
def balancedBrackets(string):
    openeingBrackets = "([{"
    closingBrackets = ")]}"
    matchingBrackets = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in string:
        if char in openeingBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if len(stack) == 0:
                return False
            if stack[-1] == matchingBrackets[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


def isBalancedBrackets(string):
    return "Balanced string" if balancedBrackets(string) else "Inbalanced string"


if __name__ == '__main__':
    print('%(string)s %(method)s' % {
          "string": "(([]()()){})",  "method": isBalancedBrackets('(([]()()){})')})
    print('%(string)s %(method)s' % {
          "string": ")[]}",  "method": isBalancedBrackets(')[]}')})
    print('%(string)s %(method)s' % {
          "string": "(()())((()()()))", "method": isBalancedBrackets("(()())((()()()))")})
    print('%(string)s %(method)s' % {"string": "(((((([[[[[[{{{{{{{{{{{{()}}}}}}}}}}}}]]]]]]))))))((([])({})[])[])[]([]){}(())", "method": isBalancedBrackets(
        "(((((([[[[[[{{{{{{{{{{{{()}}}}}}}}}}}}]]]]]]))))))((([])({})[])[])[]([]){}(())")})
    print('%(string)s %(method)s' % {
          "string": "((){{{{[]}}}})", "method": isBalancedBrackets("((){{{{[]}}}})")})
    print('%(string)s %(method)s' % {"string": "(((((({{{{{[[[[[([)])]]]]]}}}}}))))))", "method": isBalancedBrackets(
        "(((((({{{{{[[[[[([)])]]]]]}}}}}))))))")})

""" def balancedBrackets(string):
    stack = []

    for str in string:
        if str == '(' or str == '[' or str == '{':
            stack.append(str)

        if str == ')' or str == ']' or str == '}':
            bracket = stack[len(stack)-1]
            if bracket == '(':
                stack.pop()
            elif bracket == '[':
                stack.pop()
            elif bracket == '{':
                stack.pop()
    return "Balanced string" if len(stack) == 0 else "Inbalanced string" """
