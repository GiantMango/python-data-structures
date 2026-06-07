# Linked list
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f"Top: {str(self.value)}"


class Stack:
    def __init__(self):
        self.size = 0
        self.top = None

    def push(self, value):
        new_node = Node(value, self.top)
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("pop from empty stack")
        removed = self.top
        self.top = self.top.next
        self.size -= 1
        return removed

    def get_top(self):
        if self.size == 0:
            raise IndexError("Stack is empty")
        return self.top.value

    def is_empty(self):
        return self.top is None

    def contains(self, value):
        return value in self

    def __contains__(self, value):
        current = self.top

        while current:

            if value == current.value:
                return True
            current = current.next

        return False

    def __len__(self):
        return self.size

    def __str__(self):
        if self.is_empty():
            return "Empty"

        values = ["top"]
        current = self.top

        while current:
            values.append(str(current.value))
            current = current.next
        values.append("None")
        return " -> ".join(values)
