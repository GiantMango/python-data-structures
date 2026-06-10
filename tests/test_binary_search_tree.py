import pytest
import sys

sys.path.insert(0, "../src")
from binary_search_tree import BinarySearchTree


def build_sample_tree():
    """
    Builds this BST:

            10
           /  \\
          5    15
         / \\   / \\
        3   7 12 20
             \\
              8
    """
    bst = BinarySearchTree()

    for value in [10, 5, 15, 3, 7, 12, 20, 8]:
        bst.insert(value)

    return bst


def test_delete_from_empty_tree_raises_index_error():
    bst = BinarySearchTree()

    with pytest.raises(IndexError):
        bst.delete(10)


def test_delete_missing_value_raises_key_error():
    bst = build_sample_tree()

    with pytest.raises(KeyError):
        bst.delete(999)


def test_delete_leaf_node():
    bst = build_sample_tree()

    bst.delete(3)

    assert bst.in_order_traversal() == [5, 7, 8, 10, 12, 15, 20]
    assert bst.level_order_traversal() == [10, 5, 15, 7, 12, 20, 8]
    assert len(bst) == 7
    assert 3 not in bst


def test_delete_node_with_one_right_child():
    bst = build_sample_tree()

    bst.delete(7)

    assert bst.in_order_traversal() == [3, 5, 8, 10, 12, 15, 20]
    assert bst.level_order_traversal() == [10, 5, 15, 3, 8, 12, 20]
    assert len(bst) == 7
    assert 7 not in bst
    assert 8 in bst


def test_delete_node_with_two_children_direct_successor():
    bst = build_sample_tree()

    bst.delete(5)

    assert bst.in_order_traversal() == [3, 7, 8, 10, 12, 15, 20]
    assert bst.level_order_traversal() == [10, 7, 15, 3, 8, 12, 20]
    assert len(bst) == 7
    assert 5 not in bst
    assert 3 in bst
    assert 7 in bst
    assert 8 in bst


def test_delete_root_with_two_children_deep_successor():
    bst = build_sample_tree()

    bst.delete(10)

    assert bst.in_order_traversal() == [3, 5, 7, 8, 12, 15, 20]
    assert bst.level_order_traversal() == [12, 5, 15, 3, 7, 20, 8]
    assert len(bst) == 7
    assert 10 not in bst
    assert 12 in bst


def test_delete_root_when_only_one_node():
    bst = BinarySearchTree()
    bst.insert(10)

    bst.delete(10)

    assert bst.in_order_traversal() == []
    assert bst.level_order_traversal() == []
    assert len(bst) == 0
    assert 10 not in bst


def test_delete_root_with_only_left_child():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)

    bst.delete(10)

    assert bst.in_order_traversal() == [5]
    assert bst.level_order_traversal() == [5]
    assert len(bst) == 1
    assert 10 not in bst
    assert 5 in bst


def test_delete_root_with_only_right_child():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(15)

    bst.delete(10)

    assert bst.in_order_traversal() == [15]
    assert bst.level_order_traversal() == [15]
    assert len(bst) == 1
    assert 10 not in bst
    assert 15 in bst


def test_delete_all_nodes_one_by_one():
    bst = build_sample_tree()

    for value in [3, 8, 7, 5, 12, 20, 15, 10]:
        bst.delete(value)

    assert bst.in_order_traversal() == []
    assert bst.level_order_traversal() == []
    assert len(bst) == 0
