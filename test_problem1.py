from problem1 import LRUCache
from typing import final
import unittest


@final
class TestLRUCache(unittest.TestCase):
    def test_cache_with_value(self):
        cache = LRUCache[int, int](1)
        cache.set(1, 1)
        self.assertEqual(cache.get(1), 1)

    def test_cache_when_capacity_is_full(self):
        cache = LRUCache[int, int](1)
        cache.set(1, 1)
        cache.set(2, 2)

        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.get(1), None)

    def test_cache_when_capacity_is_zero(self):
        cache = LRUCache[int, int](0)

        cache.set(1, 1)
        cache.set(2, 2)

        self.assertEqual(cache.get(2), None)
        self.assertEqual(cache.get(1), None)


if __name__ == "__main__":
    unittest.main()
