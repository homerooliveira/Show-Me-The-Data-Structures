from linkedlist import LinkedList
from typing import TypeVar

_T = TypeVar("_T")


def union(llist_1: LinkedList[_T], llist_2: LinkedList[_T]) -> LinkedList[_T]:
    merged_list: LinkedList[_T] = LinkedList()

    for value in llist_1:
        merged_list.append(value)

    for value in llist_2:
        merged_list.append(value)

    return merged_list


def intersection(llist_1: LinkedList[_T], llist_2: LinkedList[_T]):
    intersected_list: LinkedList[_T] = LinkedList()
    set_of_list_1 = set(llist_1)

    for value in llist_2:
        if value in set_of_list_1:
            intersected_list.append(value)

    return intersected_list


if __name__ == "__main__":
    # Test Case 1
    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    linked_list_1: LinkedList[int] = LinkedList.fromlist(element_1)
    linked_list_2: LinkedList[int] = LinkedList.fromlist(element_2)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))

    # Test case 2
    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    linked_list_3: LinkedList[int] = LinkedList.fromlist(element_1)
    linked_list_4: LinkedList[int] = LinkedList.fromlist(element_2)

    print(union(linked_list_3, linked_list_4))
    print(intersection(linked_list_3, linked_list_4))
