class Queue:

    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if len(self.elements) == 0:
            return None
        el = self.elements[0]
        self.elements = self.elements[1:]
        return el

    def peak(self):
        if len(self.elements) == 0:
            return None
        return self.elements[0]

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return len(self.elements) == 0

    def __str__(self):
        return str(self.elements)

queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
print("Queue elements:", queue)
element = queue.pop()
print("First element-pop:", element)
print("Remained elements:", queue)
print("Size of the queue:", queue.size())
print("Is the queue empty:", queue.is_empty())
print("First element-peak:", queue.peak())
print("Size of the queue:", queue.size())
queue.pop()
queue.pop()
print("Size of the queue:", queue.size())
print("Is the queue empty:", queue.is_empty())
print("Peak:", queue.peak())
print("Pop:", queue.pop())
