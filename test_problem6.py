from problem6 import intersection, union
from linkedlist import LinkedList
from typing import List, final
import unittest


@final
class TestUnion(unittest.TestCase):
    def test_union_with_two_linked_list(self):
        element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
        element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
        expected = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21, 6, 32, 4, 9, 6, 1, 11, 21, 1]

        linked_list_1: LinkedList[int] = LinkedList.fromlist(element_1)
        linked_list_2: LinkedList[int] = LinkedList.fromlist(element_2)

        union_linked_list = union(linked_list_1, linked_list_2)

        self.assertEqual(list(union_linked_list), expected)

    def test_union_with_one_empty_linked_list(self):
        linked_list_1: LinkedList[int] = LinkedList.fromlist([1, 2, 3])
        linked_list_2: LinkedList[int] = LinkedList.fromlist([])
        expected = [1, 2, 3]

        union_linked_list = union(linked_list_1, linked_list_2)

        self.assertEqual(list(union_linked_list), expected)

    def test_union_with_two_empty_linked_list(self):
        linked_list_1: LinkedList[int] = LinkedList.fromlist([])
        linked_list_2: LinkedList[int] = LinkedList.fromlist([])
        expected: List[int] = []

        union_linked_list = union(linked_list_1, linked_list_2)

        self.assertEqual(list(union_linked_list), expected)


@final
class TestIntersection(unittest.TestCase):
    def test_intersection_with_two_linked_list(self):
        element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
        element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
        expected = [6, 4, 6, 21]

        linked_list_1: LinkedList[int] = LinkedList.fromlist(element_1)
        linked_list_2: LinkedList[int] = LinkedList.fromlist(element_2)

        intersection_linked_list = intersection(linked_list_1, linked_list_2)

        self.assertEqual(list(intersection_linked_list), expected)

    def test_intersection_without_intersected_values(self):
        element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
        element_2 = [1, 7, 8, 9, 11, 21, 1]
        expected: List[int] = []

        linked_list_1: LinkedList[int] = LinkedList.fromlist(element_1)
        linked_list_2: LinkedList[int] = LinkedList.fromlist(element_2)

        intersection_linked_list = intersection(linked_list_1, linked_list_2)

        self.assertEqual(list(intersection_linked_list), expected)

    def test_intersection_with_two_empty_linked_list(self):
        linked_list_1: LinkedList[int] = LinkedList.fromlist([])
        linked_list_2: LinkedList[int] = LinkedList.fromlist([])
        expected: List[int] = []

        intersection_linked_list = intersection(linked_list_1, linked_list_2)

        self.assertEqual(list(intersection_linked_list), expected)


if __name__ == "__main__":
    unittest.main()
