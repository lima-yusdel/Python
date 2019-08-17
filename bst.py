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
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        if self.data == data:
            return False
        else:
            if self.data < data:
                if self.right:
                    return self.right.insert(data)
                else:
                    self.right = Node(data)
            else:
                if self.left:
                    return  self.left.insert(data)
                else:
                    self.left = Node(data)


class Tree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)

    def query(self,root, target, stack):
        if root.data < target:
            if root.right != None:
                stack.push('r')
                return tree.query(root.right, target, stack)
        if root.data > target:
            if root.left != None:
                stack.push('l')
                return tree.query(root.left, target, stack)
        elif root.data == target:
            return stack
        elif root.data != target:
            return None



def main():
    global tree
    global stack
    global head
    stack = Stack()
    tree = Tree()
    path = []
    init = True

    while init:
        try:
            inputData = str(input()).split(' ')
        except EOFError:
            quit()
        if inputData[0] == 'i':
            init = False
            head =  int(inputData[1])
            tree.insert(int(inputData[1]))
        else:
            print('invalid command')

    while True:
        path = ['']
        try:
            inputData = str(input()).split(' ')
        except EOFError:
            quit()
        if inputData[0] == 'i':
            tree.insert(int(inputData[1]))
        elif inputData[0] == 'q':
            target = int(inputData[1])
            stack = tree.query(tree.root, target, stack)
            if stack != None:
                for items in range(stack.size()):
                    number = stack.pop()
                    path.append(number)

                if path == ['']:
                    print('found: root')
                else:
                    print('found: ' + ' '.join(reversed(path)))

                for items in range(stack.size()):
                    stack.items.remove(items)
            else:
                    print('not found')
                    stack = Stack()
        else:
            print('invalid command')

main()
