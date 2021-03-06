from dataclasses import dataclass, field
from datetime import datetime
import hashlib
from typing import Optional, final
from pprint import pprint
from linkedlist import LinkedList


@dataclass
class Block:
    data: str
    timestamp: datetime = field(default=datetime.utcnow())
    previous_hash: Optional[str] = None
    hash: str = field(init=False)

    def __post_init__(self):
        self.hash = self.calc_hash()

    def calc_hash(self) -> str:
        sha = hashlib.sha256()

        hash_str: bytes = self.data.encode("utf-8")
        hash_str += self.timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%Z").encode("utf-8")

        if previous_hash := self.previous_hash:
            hash_str += previous_hash.encode("utf-8")

        sha.update(hash_str)

        return sha.hexdigest()


@final
class Blockchain:
    chain: LinkedList[Block]

    def __init__(self):
        self.chain = LinkedList()

    def add(self, data: str):
        previous_hash: Optional[str] = None

        if self.chain.tail:
            previous_hash = self.chain.tail.value.hash

        self.chain.append(Block(data, previous_hash=previous_hash))

    def __repr__(self) -> str:
        return str(self.chain)


if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.add("test with string")
    blockchain.add("test with string")
    blockchain.add("test with string")

    pprint(list(blockchain.chain))
