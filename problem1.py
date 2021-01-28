from typing import Dict, Generic, Optional, TypeVar, final


_K = TypeVar('_K')
_V = TypeVar('_V')

@final
class _Node(Generic[_K, _V]):
    next: Optional['_Node[_K, _V]']
    previous: Optional['_Node[_K, _V]']
    key: _K
    value: _V

    def __init__(self, key: _K, value: _V):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

    def __repr__(self):
        return f"[key={self.key}, value={self.value}]"

@final
class LRUCache(Generic[_K, _V]):
    """
    Implementation based on `https://krishankantsinghal.medium.com/my-first-blog-on-medium-583159139237`
    """

    _head: Optional[_Node[_K, _V]]
    _tail: Optional[_Node[_K, _V]]
    _dict: Dict[_K, _Node[_K, _V]]
    capacity: int

    def __init__(self, capacity: int):
        self._head = None
        self._tail = None
        self._dict = {}
        self.capacity = capacity

    def get(self, key: _K) -> Optional[_V]:
        if key not in self._dict:
            return None

        node = self._dict[key]
        
        if node is not self._head:
            self._remove(node)
            self._add_first(node)
        
        return node.value

    def set(self, key: _K, value: _V):
        if self.capacity == 0:
            return

        if key in self._dict:
            node = self._dict[key]
            node.value = value
            self._remove(node)
            self._add_first(node)
        else:
            node = _Node(key, value)
            if len(self._dict) == self.capacity:
                del self._dict[self._tail.key] # type: ignore
                self._remove(self._tail) # type: ignore
            self._add_first(node)
            self._dict[key] = node

    def _add_first(self, node: _Node[_K, _V]):
        node.previous = None

        if self._head is None:
            self._head = node
            self._tail = node
        else:
            node.next = self._head
            self._head.previous = node
            self._head = node

    def _remove(self, node: _Node[_K, _V]):
        if node.previous:
            node.previous.next = node.next
        else:
            self._head = node.next

        if node.next:
            node.next.previous = node.previous
        else:
            self._tail = node.previous

if __name__ == "__main__":
    our_cache: LRUCache[int, int] = LRUCache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    print(our_cache.get(1))       # returns 1
    print(our_cache.get(2))       # returns 2
    print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
