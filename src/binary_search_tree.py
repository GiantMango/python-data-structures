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
        return str(self.value)

    def __repr__(self):
        return str(self.value)


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

        parent, current = self._find_node_and_parent(value)

        if current.left is None and current.right is None:  # 1. deleting a leaf node
            self._replace_parent_child(parent, current, None)
        elif current.left is None:  # 2. deleting a node with 1 child on the right
            self._replace_parent_child(parent, current, current.right)
        elif current.right is None:  # 2. deleting a node with 1 child on the left
            self._replace_parent_child(parent, current, current.left)
        else:  # 3. deleting a node with 2 children
            new_child = self._find_min_node(current.right)
            new_parent, _ = self._find_node_and_parent(new_child.value)
            current.value = new_child.value
            if new_parent.right == new_child:
                new_parent.right = new_child.right
            elif new_parent.left == new_child:
                new_parent.left = new_child.right

        self.size -= 1

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

    def _find_node_and_parent(self, value):
        current = self.root
        parent = None

        while current is not None:
            if value == current.value:
                return (parent, current)
            elif value > current.value:
                parent = current
                current = current.right
            else:
                parent = current
                current = current.left

        raise KeyError(value)

    def _replace_parent_child(self, parent, current, new):
        if current == self.root:
            self.root = new
            return
        if parent.right == current:
            parent.right = new
        elif parent.left == current:
            parent.left = new

    def _height(self):
        raise NotImplementedError

    def __contains__(self, value):
        current = self.root

        while current is not None:
            if value == current.value:
                return True
            elif value > current.value:
                current = current.right
            else:
                current = current.left
        return False

    def __len__(self):
        return self.size

    def __str__(self):
        if self.root is None:
            return "Empty"

        values = []
        return "->".join(values)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(7)
    bst.insert(3)
    bst.insert(12)
    bst.insert(20)
    bst.insert(13)
    bst.insert(8)
    print(bst.level_order_traversal())

    bst.delete(10)
    print(bst.level_order_traversal())
    bst.delete(5)

    print(bst.level_order_traversal())
    bst.delete(15)
    print(bst.level_order_traversal())
