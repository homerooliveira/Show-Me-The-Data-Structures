from typing import Generic, Iterable, Iterator, List, Optional, Sized, TypeVar, final


T = TypeVar("T")


@final
class Node(Generic[T]):
    next: Optional["Node[T]"]
    value: T

    def __init__(self, value: T):
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return str(self.value)


@final
class LinkedList(Iterable[T], Sized, Generic[T]):
    head: Optional[Node[T]]
    tail: Optional[Node[T]]
    size: int = 0

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value: T):
        node = Node(value)

        if self.tail is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    def __iter__(self) -> Iterator[T]:
        current = self.head

        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        return " -> ".join([str(value) for value in self])

    @classmethod
    def fromlist(cls, list: List[T]) -> "LinkedList[T]":
        linked_list: LinkedList[T] = cls()

        for value in list:
            linked_list.append(value)

        return linked_list
