from typing import Generic, Iterable, Iterator, Optional, TypeVar, final


T = TypeVar('T')

@final
class Node(Generic[T]):
    next: Optional['Node[T]']
    value: T

    def __init__(self, value: T):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


@final
class LinkedList(Iterable[T], Generic[T]):
    head: Optional[Node[T]]

    def __init__(self):
        self.head = None

    def __str__(self) -> str:
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value: T):
        
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self) -> int:
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    def __iter__(self) -> Iterator[T]:
        current = self.head

        while current is not None:
            yield current.value
            current = current.next

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