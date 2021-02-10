import os
from typing import List
import pprint


def find_files(suffix: str, path: str) -> List[str]:
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    paths: List[str] = []

    if os.path.isfile(path) and path.endswith(suffix):
        return [path]
    elif os.path.isdir(path):
        for subpath in os.listdir(path):
            paths.extend(find_files(suffix, os.path.join(path, subpath)))

    return paths


if __name__ == "__main__":
    pprint.pprint(find_files(".c", "./testdir"))
