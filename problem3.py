from dataclasses import dataclass, field
import heapq
import sys
from typing import Counter, Dict, Optional, Tuple

@dataclass(order=True)
class _Node:
    frequency: int
    char: Optional[str] = field(compare=False)
    left: Optional['_Node'] = field(default=None, compare=False, repr=False)
    right: Optional['_Node'] = field(default=None, compare=False, repr=False)

def huffman_encoding(data: str) -> Tuple[str, _Node]:
    if len(data) == 0:
        raise ValueError("Data must be not empty.")

    nodes = [_Node(item[1], item[0]) for item in Counter(data).items()]

    heapq.heapify(nodes)

    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        new_node = _Node(left.frequency + right.frequency, None, left, right)
        heapq.heappush(nodes, new_node)
    
    # Special case when string have single character
    if len(nodes) == 1 and nodes[0].char is not None: 
        left = nodes[0]
        new_node = _Node(left.frequency + 1, None, left, None)
        nodes[0] = new_node

    codes: Dict[str, str] = {}

    _create_codes(codes, nodes[0], "")

    binaryStr = "".join(map(lambda x: codes.get(x, ""), data))

    return (binaryStr, nodes[0])

def _create_codes(codes: Dict[str, str], node: Optional[_Node], binaryStr: str):
    if node is None:
        return
    
    if node.char:
        codes[node.char] = binaryStr
    else:
        _create_codes(codes, node.left, binaryStr + "0")
        _create_codes(codes, node.right, binaryStr + "1")

def huffman_decoding(data: str, tree: _Node) -> str:
    decoded_data = ""
    start_index = 0
    end_index = 1
    
    while start_index != len(data):
        sub_data = data[start_index:end_index]
        if decoded_str := _find_code(sub_data, tree):
            decoded_data += decoded_str
            start_index = end_index
        
        end_index += 1

    return decoded_data

def _find_code(data: str, node: Optional[_Node]) -> Optional[str]:
    if node is None:
        return None
    
    if node.left is None and node.right is None:
        return node.char
    
    if len(data) == 0:
        return None

    if data[0] == "0":
        return _find_code(data[1:], node.left)
    elif data[0] == "1":
        return _find_code(data[1:], node.right)


if __name__ == "__main__":
    # a_great_sentence = "The bird is the word"
    a_great_sentence = "AA"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The content of the encoded data is: {}\n".format(encoded_data))
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))