# Analytic Problem 1

The time-complexity for `get` and `set` are `O(1)` and space-complexity is `O(N)`.

For the `get` method first I need check if the key exist in the dictionary, if exist I get the node and validate if is not head node I add the node to start of linked list then I return the value if not exist I return `None`.

For the `set` method first I ensure the capacity is greather than zero, if the key exist I get node, update the value and add to start of linked list, if not exist I create a new node check if capacity is max I will remove the last node after that I add node to start of linked list and node to dictionary.

I use doubly linked list to `add` and `remove` to be `O(1)` and dictionary to find the node using the key to be `O(1)`.