# Analytic Problem 1

The time-complexity for `get` and `set` is  `O(1)` and space-complexity is `O(N)`.

For the `get` method first we need check if the key exist in the dictionary, if exist we get the node and validate if is not head node we add the node to start of linked list then we return the value if not exist we return `None`.

For the `set` method first we ensure the capacity is greather than zero, if the key exist we get node, update the value and add to start of linked list, if not exist we create a new node check if capacity is max we will remove the last node after that we add node to start of linked list and node to dictionary.

We use doubly linked list to `add` and `remove` to be `O(1)` and dictionary to find the node using the key to be `O(1)`.