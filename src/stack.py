# Linked list
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.size = 0
        self.top = None


stack = Stack()
print(stack)
