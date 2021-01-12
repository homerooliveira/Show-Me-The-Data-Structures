from linkedlist import LinkedList
from typing import TypeVar

T = TypeVar('T')

def union(llist_1: LinkedList[T], llist_2: LinkedList[T]) -> LinkedList[T]:
    merged_list: LinkedList[T] = LinkedList()

    for value in llist_1:
        merged_list.append(value)
    
    for value in llist_2:
        merged_list.append(value)

    return merged_list

def intersection(llist_1: LinkedList[T], llist_2: LinkedList[T]):
    intersected_list: LinkedList[T] = LinkedList()

    set_of_list_1 = set(llist_1)

    for value in llist_2:
        if value in set_of_list_1:
            intersected_list.append(value)

    return intersected_list

if __name__ == "__main__":
    # Test Case 1

    linked_list_1: LinkedList[int] = LinkedList()
    linked_list_2: LinkedList[int] = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1,linked_list_2))
    print(intersection(linked_list_1,linked_list_2))

    # Test case 2

    linked_list_3: LinkedList[int] = LinkedList()
    linked_list_4: LinkedList[int] = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3,linked_list_4))
    print(intersection(linked_list_3,linked_list_4))