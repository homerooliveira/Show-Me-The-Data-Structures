from typing import Generic, Optional, TypeVar, final


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
class LinkedList(Generic[T]):
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