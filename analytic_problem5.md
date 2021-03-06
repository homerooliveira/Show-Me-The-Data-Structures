## Problem 5

The time-complexity and space-complexity for this program are `O(1)` because the `add` method of linked list is `O(1)`.

I prefer to use a linked list to represent a blockchain because it flows the same abstraction as the blockchain. For the `add` method I check if there is the last element in the list and I take the element to generate the previous hash, then I create a new `Block` with data and the previous hash, the hash is calculated after `init` using data, timestamp and previous hash if it is not null.