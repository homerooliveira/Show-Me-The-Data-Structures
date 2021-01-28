from problem3 import huffman_decoding, huffman_encoding
from typing import final
import unittest


@final
class TestHuffmanCode(unittest.TestCase):

    def test_encoding(self):
        string = "AAAAAAABBBCCCCCCCDDEEEEEE"
        expected = "1010101010101000100100111111111111111000000010101010101"
        
        (encoding_str, _) = huffman_encoding(string)

        self.assertEqual(encoding_str, expected)

    def test_decoding(self):
        string = "1010101010101000100100111111111111111000000010101010101"
        expected = "AAAAAAABBBCCCCCCCDDEEEEEE"
        
        (_, node)= huffman_encoding(expected)
        decoding_str = huffman_decoding(string, node)

        self.assertEqual(decoding_str, expected)
    
    def test_encoding_single_char(self):
        string = "AAA"
        expected = "000"
        
        (encoding_str, _) = huffman_encoding(string)

        self.assertEqual(encoding_str, expected)

    def test_decoding_single_char(self):
        string = "000"
        expected = "AAA"
        
        (_, node)= huffman_encoding(expected)
        decoding_str = huffman_decoding(string, node)
        
        self.assertEqual(decoding_str, expected)

    def test_encoding_empty_str(self):
        with self.assertRaises(ValueError) as context:
            huffman_encoding("")


        self.assertEqual(str(context.exception), "Data must be not empty.")

if __name__ == '__main__':
    unittest.main()