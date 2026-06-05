class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return "ListNode {val: " + str(self.value) + ", next: " + str(self.next) + "}"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_last(self, value):
        new_node = Node(value, None)

        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def add_first(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        self.size += 1

    def remove_first(self):
        if self.size == 0:
            raise IndexError("remove_first from empty list")
        else:
            removed_value = self.head.value
            self.head = self.head.next

        self.size -= 1
        return removed_value

    def remove_last(self):
        if self.size == 0:
            raise IndexError("remove_last from empty list")
        else:
            removed_value = self.tail.value
            current = self.head
            while current.next.next is not None:
                current = current.next
            self.tail = current
            self.tail.next = None
        self.size -= 1
        return removed_value

    def peek_first(self):
        return self.head.value

    def peek_last(self):
        return self.tail.value

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def to_list(self):
        ls = []
        current = self.head
        while current:
            ls.append(current.value)
            current = current.next
        return ls

    def is_empty(self):
        return self.size == 0

    def find(self, value):
        current = self.head
        i = 0
        while current:
            if current.value == value:
                return i
            current = current.next
            i += 1
        return -1

    def get_value(self, ind):
        current = self.head
        if ind >= self.size:
            raise IndexError("index out of range")
        else:
            for _ in range(ind):
                current = current.next

        return current.value

    def insert(self, ind, value):
        current = self.head
        if ind >= self.size:
            raise IndexError("index out of range")
        else:
            for _ in range(ind):
                current = current.next
        old_next = current.next
        current.next = Node(value, old_next)
        self.size += 1

    def reverse(self):
        self.tail = self.head
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def contains(self, value):
        return value in self

    def __contains__(self, value):
        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next

        return False

    def __len__(self):
        return self.size

    def __str__(self):
        if self.head is None:
            return "Empty"

        values = ["head"]
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        values.append("None")
        return " -> ".join(values)
