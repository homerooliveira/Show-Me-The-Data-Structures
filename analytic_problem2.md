## Problem 2

The time-complexity for this program is `O(N)`, `N` is total number of files and folders, space-complexity is `O(N)` `N` is the number of files with suffix passed by user. 

First I check if path is a file and path end with suffix then I will return a list with a path, else I will check if path is directory and will iterate over all paths from this directory adding to paths list calling the same method recursive, end of method I will return the paths.