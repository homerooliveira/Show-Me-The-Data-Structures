## Problem 6

The time complexity and space complexity for `union` are `O (n + m)` because the `n` is the length of the first list and `m` is the length of the second list. I create a new list to represent the merged list and then iterate through the two lists by adding the elements. 

The time complexity for `intersection` is `O (n)` because
we are using `set` to check if the element exists in another list. I create the `set` of the first list to be quick to check for elements in that list, so I will iterate through the second list and if the element of the second exists in the first list I will add it to the intersection list.