import unittest
from Lab3_1 import DoublyLinkedList
from Lab3_1 import split_list
class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.L = DoublyLinkedList()
        self.L.add_node(1)
        self.L.add_node(-2)
        self.L.add_node(3)
        self.L.add_node(-4)
        self.L.add_node(5)

    def test_add_node(self):
        self.assertEqual(self.L.head.value, 1)
        self.assertEqual(self.L.tail.value, 5)
        self.assertEqual(self.L.head.next.value, -2)
        self.assertEqual(self.L.tail.prev.value, -4)

    def test_split_list(self):
        L1, L2 = split_list(self.L)
        self.assertEqual(L1.head.value, 1)
        self.assertEqual(L1.tail.value, 5)
        self.assertEqual(L1.head.next.value, 3)
        self.assertIsNone(L1.tail.next)
        self.assertEqual(L2.head.value, -2)
        self.assertEqual(L2.tail.value, -4)
        self.assertEqual(L2.head.next.value, -4)
        self.assertIsNone(L2.tail.next)

if __name__ == '__main__':
    unittest.main()
