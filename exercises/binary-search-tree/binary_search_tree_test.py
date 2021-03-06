import unittest

from binary_search_tree import BinarySearchTree


class BinarySearchTreeTests(unittest.TestCase):
    def test_add_one_value_in_tree(self):
        tree = BinarySearchTree()
        self.assertEqual(tree.add(3), True)
        self.assertEqual(tree.size(), 1)
        self.assertEqual(tree.contains(3), True)

    def test_add_multiple_values_in_tree(self):
        tree = BinarySearchTree()
        self.assertEqual(tree.add(-1), True)
        self.assertEqual(tree.add(50), True)
        self.assertEqual(tree.add(-73), True)
        self.assertEqual(tree.add(20), True)
        self.assertEqual(tree.size(), 4)
        self.assertEqual(tree.contains(-1), True)
        self.assertEqual(tree.contains(50), True)
        self.assertEqual(tree.contains(-73), True)
        self.assertEqual(tree.contains(20), True)

    def test_add_repeated_values_in_tree(self):
        tree = BinarySearchTree()
        self.assertEqual(tree.add(2), True)
        self.assertEqual(tree.add(3), True)
        self.assertEqual(tree.add(4), True)
        self.assertEqual(tree.add(2), False)
        self.assertEqual(tree.add(1), True)
        self.assertEqual(tree.add(1), False)
        self.assertEqual(tree.add(1), False)
        self.assertEqual(tree.add(2), False)
        self.assertEqual(tree.add(3), False)
        self.assertEqual(tree.add(4), False)
        self.assertEqual(tree.add(5), True)
        self.assertEqual(tree.size(), 5)
        self.assertEqual(tree.contains(1), True)
        self.assertEqual(tree.contains(2), True)
        self.assertEqual(tree.contains(3), True)
        self.assertEqual(tree.contains(4), True)
        self.assertEqual(tree.contains(5), True)

    def test_remove_one_value_in_tree_with_no_elements(self):
        tree = BinarySearchTree()
        self.assertEqual(tree.remove(70), False)
        self.assertEqual(tree.size(), 0)
        self.assertEqual(tree.contains(70), False)

    def test_remove_multiple_values_in_tree_with_no_elements(self):
        tree = BinarySearchTree()
        self.assertEqual(tree.remove(70), False)
        self.assertEqual(tree.remove(-25), False)
        self.assertEqual(tree.size(), 0)
        self.assertEqual(tree.contains(70), False)
        self.assertEqual(tree.contains(-25), False)

    def test_remove_value_in_tree_with_one_element(self):
        tree = BinarySearchTree()
        tree.add(0)
        self.assertEqual(tree.remove(0), True)
        self.assertEqual(tree.size(), 0)
        self.assertEqual(tree.contains(0), False)

    def test_remove_multiple_values_in_tree(self):
        tree = BinarySearchTree()
        tree.add(3)
        tree.add(1)
        tree.add(2)
        tree.add(5)
        tree.add(4)
        self.assertEqual(tree.remove(3), True)
        self.assertEqual(tree.remove(1), True)
        self.assertEqual(tree.remove(5), True)
        self.assertEqual(tree.remove(6), False)
        self.assertEqual(tree.remove(7), False)
        self.assertEqual(tree.size(), 2)
        self.assertEqual(tree.contains(1), False)
        self.assertEqual(tree.contains(2), True)
        self.assertEqual(tree.contains(3), False)
        self.assertEqual(tree.contains(4), True)
        self.assertEqual(tree.contains(5), False)
        self.assertEqual(tree.contains(6), False)
        self.assertEqual(tree.contains(7), False)

    def test_contains_value_in_tree_with_no_elements(self):
        tree = BinarySearchTree()
        self.assertEqual(tree.contains(-123), False)
        self.assertEqual(tree.contains(-0), False)

    def test_contains_value_in_tree_with_multiple_operations(self):
        tree = BinarySearchTree()
        tree.remove(1)
        self.assertEqual(tree.contains(1), False)
        tree.add(1)
        self.assertEqual(tree.contains(1), True)
        tree.remove(2)
        self.assertEqual(tree.contains(2), False)
        tree.add(3)
        self.assertEqual(tree.contains(3), True)
        tree.add(2)
        self.assertEqual(tree.contains(2), True)
        tree.add(4)
        self.assertEqual(tree.contains(4), True)
        tree.remove(1)
        self.assertEqual(tree.contains(1), False)
        tree.remove(1)
        self.assertEqual(tree.contains(1), False)
        tree.add(2)
        self.assertEqual(tree.contains(2), True)
        tree.add(5)
        self.assertEqual(tree.contains(5), True)
        tree.remove(2)
        self.assertEqual(tree.contains(1), False)
        self.assertEqual(tree.contains(2), False)
        self.assertEqual(tree.contains(3), True)
        self.assertEqual(tree.contains(4), True)
        self.assertEqual(tree.contains(5), True)

    def test_size_in_tree_with_no_elements(self):
        tree = BinarySearchTree()
        self.assertEqual(tree.size(), 0)

    def test_size_in_tree_with_multiple_operations(self):
        tree = BinarySearchTree()
        self.assertEqual(tree.size(), 0)
        tree.add(1)
        self.assertEqual(tree.size(), 1)
        tree.remove(1)
        self.assertEqual(tree.size(), 0)
        tree.remove(2)
        self.assertEqual(tree.size(), 0)
        tree.add(3)
        self.assertEqual(tree.size(), 1)
        tree.add(2)
        self.assertEqual(tree.size(), 2)
        tree.add(4)
        self.assertEqual(tree.size(), 3)
        tree.remove(1)
        self.assertEqual(tree.size(), 3)
        tree.remove(1)
        self.assertEqual(tree.size(), 3)
        tree.add(2)
        self.assertEqual(tree.size(), 3)
        tree.add(5)
        self.assertEqual(tree.size(), 4)
        tree.remove(2)
        self.assertEqual(tree.size(), 3)


if __name__ == '__main__':
    unittest.main()
