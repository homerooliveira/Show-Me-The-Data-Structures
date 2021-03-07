## Problem 3

The time complexity for `encoding` is `O(N log N)` , space complexity for `endoding` id `O(N)`. First I create `Counter` to create frenquency list, after that I create list of nodes, then will use heap to create the tree, next I will create dictonary to represent the code of the letter, finaly I will use the dictonary to encode the string.

The time complexity for `decode` is `O(N)`, space complexity for `decoding` is `O(N)`. Firt I create `start_index` and `end_index` to represent current subString to try decode, then I will create the subString and I will try to find code using the tree, using pre order to find code if is found a append on decoded string and `star_index` will receive the `end_index`, every iteration I will increment one in `end_index`.