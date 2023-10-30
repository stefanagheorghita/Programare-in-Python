class Stack:
    elements = []

    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if len(self.elements) == 0:
            return None
        el = self.elements[-1]
        self.elements = self.elements[:-1]
        return el

    def peak(self):
        if len(self.elements) == 0:
            return None
        return self.elements[-1]

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return len(self.elements) == 0

    def __str__(self):
        return str(self.elements)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack elements:", stack)
element = stack.pop()
print("Last element-pop:", element)
print("Remained elements:", stack.elements)
print("Size of the stack:", stack.size())
print("Is the stack empty:", stack.is_empty())
print("Last element-peak:", stack.peak())
print("Size of the stack:", stack.size())
stack.pop()
stack.pop()
print("Size of the stack:", stack.size())
print("Is the stack empty:", stack.is_empty())
print("Peak:", stack.peak())
print("Pop:", stack.pop())
