from typing import final
from problem5 import Blockchain
import unittest


@final
class TestBlockchain(unittest.TestCase):
    def test_add_blockchain(self):
        blockchain = Blockchain()

        blockchain.add("1")
        blockchain.add("2")

        datas = [block.data for block in blockchain.chain]
        self.assertEqual(datas, ["1", "2"])

    def test_add_blockchain_empty(self):
        blockchain = Blockchain()

        self.assertEqual(len(blockchain.chain), 0)


if __name__ == "__main__":
    unittest.main()
