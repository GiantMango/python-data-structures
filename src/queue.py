class Node:
    def __init__(self, value, next=None):
        self.value = None
        self.next = None

    def __str__(self):
        return f"Front: {self.value}"
