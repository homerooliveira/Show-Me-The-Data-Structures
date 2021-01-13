from typing import Dict, Generic, Optional, TypeVar, final


K = TypeVar('K')
V = TypeVar('V')

@final
class _Entry(Generic[K, V]):
    next: Optional['_Entry[K, V]']
    previous: Optional['_Entry[K, V]']
    key: K
    value: V

    def __init__(self, key: K, value: V):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

    def __repr__(self):
        return f"[key={self.key}, value={self.value}]"

@final
class LRUCache(Generic[K, V]):
    """
    Implementation based on `https://krishankantsinghal.medium.com/my-first-blog-on-medium-583159139237`
    """

    _head: Optional[_Entry[K, V]]
    _tail: Optional[_Entry[K, V]]
    _dict: Dict[K, _Entry[K, V]]
    capacity: int

    def __init__(self, capacity: int):
        self._head = None
        self._tail = None
        self._dict = {}
        self.capacity = capacity
        if self.capacity < 1:
            raise ValueError('Capacity must be at least 1')

    def get(self, key: K) -> Optional[V]:
        if key not in self._dict:
            return None

        entry = self._dict[key]
        
        if entry is not self._head:
            self._remove(entry)
            self._add_first(entry)
        
        return entry.value

    def set(self, key: K, value: V):
        if key in self._dict:
            entry = self._dict[key]
            entry.value = value
            self._remove(entry)
            self._add_first(entry)
        else:
            entry = _Entry(key, value)
            if len(self._dict) == self.capacity:
                del self._dict[self._tail.key]
                self._remove(self._tail)
            self._add_first(entry)
            self._dict[key] = entry

    def _add_first(self, entry: _Entry[K, V]):
        entry.previous = None

        if self._head is None:
            self._head = entry
            self._tail = entry
        else:
            entry.next = self._head
            self._head.previous = entry
            self._head = entry

    def _remove(self, entry: _Entry[K, V]):
        if entry.previous:
            entry.previous.next = entry.next
        else:
            self._head = entry.next

        if entry.next:
            entry.next.previous = entry.previous
        else:
            self._tail = entry.previous
    
    def print(self):
        current = self._head

        while current:
            print(current, end=" ")
            current = current.next
        print()

        current = self._tail
        while current:
            print(current, end=" ")
            current = current.previous

        print()
if __name__ == "__main__":
    our_cache: LRUCache[int, int] = LRUCache(0)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    our_cache.get(1)       # returns 1
    our_cache.get(2)       # returns 2
    our_cache.get(9)      # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    our_cache.get(3)
    our_cache.print()