"""
Binary Search Tree (BST)

    A
   /\\    ---> B < A < C
  B   C

Smaller values on the left, larger values on the right
"""

from queue import Queue


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return self.value


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        if self.root is None:  # Empty tree
            self.root = Node(value)
            self.size += 1
            return

        current = self.root

        while True:
            if value > current.value:
                if current.right is None:
                    current.right = Node(value)
                    self.size += 1
                    return
                current = current.right
            elif value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    self.size += 1
                    return
                current = current.left
            else:
                raise ValueError("Duplicate value")

    def delete(self, value):
        """
        1. Deleting a leaf node
        2. Deleting a node with 1 child
        3. Deleting a node with 2 children
        """
        if self.size == 0:
            raise IndexError("delete from empty tree")

        current = self.root
        parent = self.root

    def in_order_traversal(self):
        """
        Depth-first search: Left -> Root -> Right
        """
        re = []

        def traversal(node):
            if node is None:
                return

            traversal(node.left)
            re.append(node.value)
            traversal(node.right)

        traversal(self.root)

        return re

    def pre_order_traversal(self):
        """
        Depth-first search: Root -> Left -> Right
        """
        re = []

        def traversal(node):
            if node is None:
                return
            re.append(node.value)
            traversal(node.left)
            traversal(node.right)

        traversal(self.root)
        return re

    def post_order_traversal(self):
        """
        Depth-first search: Left -> Right -> Root
        """
        re = []

        def traversal(node):
            if node is None:
                return
            traversal(node.left)
            traversal(node.right)
            re.append(node.value)

        traversal(self.root)
        return re

    def level_order_traversal(self):
        """
        Breadth-first search
        """
        queue = Queue()
        re = []
        if self.root is None:
            return re

        queue.enqueue(self.root)

        while len(queue) != 0:
            parent = queue.get_front()
            re.append(parent.value)
            if parent.left is not None:
                queue.enqueue(parent.left)
            if parent.right is not None:
                queue.enqueue(parent.right)
            queue.dequeue()

        return re

    def find_min(self):
        if self.size == 0:
            raise IndexError("find min from empty tree")
        return self._find_min_node(self.root).value

    def find_max(self):
        if self.size == 0:
            raise IndexError("find max from empty tree")
        return self._find_max_node(self.root).value

    def _find_min_node(self, node):
        if node is None:
            raise IndexError("find min node from empty subtree")

        current = node
        while current.left is not None:
            current = current.left
        return current

    def _find_max_node(self, node):
        if node is None:
            raise IndexError("find max node from empty subtree")

        current = node
        while current.right is not None:
            current = current.right
        return current

    def _height(self):
        raise NotImplementedError

    def __contains__(self, value):
        raise NotImplementedError

    def __len__(self):
        return self.size

    def __str__(self):
        if self.root is None:
            return "Empty"

        current = self.root
        values = []
        return "->".join(values)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(12)
    bst.insert(20)
    bst.insert(8)

    print(bst.in_order_traversal())
    print(bst.pre_order_traversal())
    print(bst.post_order_traversal())
    print(bst.level_order_traversal())
