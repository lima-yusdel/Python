#! /usr/bin/env python3
#by Yusdel Lima Lorenzo Prin Prog 2019
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
class Calculator:
    def main():
        stack = Stack()
        while True:
            result = 0
            try:
                element = str(input())
            except EOFError:
                quit()
            if element in ['+','-','*','/']:
                if stack.size() <= 1:
                    print('invalid operation')
                else:
                    try:
                        num1 = stack.pop()
                        num2 = stack.pop()
                        stack.push(str(eval(str(num2 + element + num1))))
                        print(stack.peek())
                    except ZeroDivisionError:
                        stack.push(num2)
                        stack.push(num1)
                        print('error: division by zero')
            else:
                if element.isdigit():
                    stack.push(element)
                    print(stack.peek())
                elif element == '~' and stack.size() >= 1:
                    number = stack.pop()
                    number = int(number)*-1
                    stack.push(str(number))
                    print(stack.peek())

                else:
                    pass
    main()
