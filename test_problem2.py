from typing import Final, final
from problem2 import find_files
import unittest


@final
class TestFindFiles(unittest.TestCase):

    valid_dir: Final[str] = "./testdir"
    invalid_dir: Final[str] = ".testdir"

    def test_empty_suffix(self):
        expected = [
            "./testdir/.DS_Store",
            "./testdir/subdir4/.gitkeep",
            "./testdir/subdir3/subsubdir1/b.h",
            "./testdir/subdir3/subsubdir1/b.c",
            "./testdir/t1.c",
            "./testdir/subdir2/.gitkeep",
            "./testdir/subdir5/a.h",
            "./testdir/subdir5/a.c",
            "./testdir/t1.h",
            "./testdir/subdir1/a.h",
            "./testdir/subdir1/a.c",
        ]
        self.assertEqual(find_files("", self.valid_dir), expected)

    def test_c_files_suffix(self):
        expected = [
            "./testdir/subdir3/subsubdir1/b.c",
            "./testdir/t1.c",
            "./testdir/subdir5/a.c",
            "./testdir/subdir1/a.c",
        ]
        self.assertEqual(find_files(".c", self.valid_dir), expected)

    def test_invalid_path(self):
        self.assertEqual(find_files(".c", self.invalid_dir), [])


if __name__ == "__main__":
    unittest.main()
