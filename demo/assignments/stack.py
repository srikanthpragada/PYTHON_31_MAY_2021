class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def length(self):
        return len(self.data)

    def empty(self):
        self.data.clear()

    def isempty(self):
        return len(self.data)  == 0


s1 = Stack()
s2 = Stack()
s1.push(5)
s1.push(100)
s2.push(10)
print(s1.peek())
print(s1.pop())
print(s1.pop())
print(s1.isempty())

