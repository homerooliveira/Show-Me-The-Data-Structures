## Problem 4

The time complexity for this program is `O (n ^ k)` because `n` is the number of groups and `k` is the depth of the group, the space complexity is `O (n)` because `n` it is the depth of the groups.

First I will iterate through the list of users if I find the username I will return `True`, otherwise, I will call the method recursively if the recursion finds the username I will return `True`, if I do not find the username I will return `False`.