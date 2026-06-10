class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class Queue:
    def __init__(self):
        self.size = 0
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError("Queue is empty.")
        removed = self.front
        self.front = self.front.next
        self.size -= 1
        if self.size == 0:
            self.rear = None
        return removed.value

    def get_front(self):
        if self.size == 0:
            raise IndexError("Queue is empty.")
        return self.front.value

    def get_rear(self):
        if self.size == 0:
            raise IndexError("Queue is empty")
        return self.rear.value

    def is_empty(self):
        return self.size == 0

    def contains(self, value):
        return value in self

    def __contains__(self, value):
        current = self.front

        while current:
            if current.value == value:
                return True
            current = current.next

        return False

    def __len__(self):
        return self.size

    def __str__(self):
        if self.is_empty():
            return "Empty"

        values = ["front"]
        current = self.front

        while current is not None:
            values.append(str(current.value))
            current = current.next

        values.append("None")
        return " -> ".join(values)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.dequeue()
    q.enqueue(30)
    q.enqueue(44)
    print(q)
