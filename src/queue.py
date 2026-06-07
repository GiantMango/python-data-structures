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
        self.front = self.front.next
        self.size -= 1

    def get_front(self):
        if self.size == 0:
            raise IndexError("Queue is empty.")
        return self.front

    def get_rear(self):
        if self.size == 0:
            raise IndexError("Queue is empty")
        return self.rear

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


q = Queue()
print("dequeue empty: ", q.dequeue())

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print("enqueue: ", q)

q.dequeue()
print("dequeue: ", q)

print("front: ", q.get_front())
print("rear: ", q.get_rear())
print("length: ", len(q))
print("contains 15: ", 15 in q)
print("contains 20: ", 20 in q)
