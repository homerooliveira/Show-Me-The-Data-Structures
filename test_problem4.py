from problem4 import Group, is_user_in_group
from typing import final
import unittest


@final
class TestIsUserInGroup(unittest.TestCase):
    def test_is_user_in_group_with_valid_user(self):
        parent = Group("parent")
        child = Group("child")
        sub_child = Group("subchild")

        sub_child_user = "sub_child_user"
        sub_child.add_user(sub_child_user)

        child.add_group(sub_child)
        parent.add_group(child)

        self.assertTrue(is_user_in_group(sub_child_user, parent))

    def test_is_user_in_group_with_invalid_user(self):
        parent = Group("parent")
        child = Group("child")
        sub_child = Group("subchild")

        sub_child_user = "sub_child_user"
        sub_child.add_user(sub_child_user)

        child.add_group(sub_child)
        parent.add_group(child)

        self.assertFalse(is_user_in_group("invalid_sub_child_user", parent))

    def test_is_user_in_group_with_empty_group(self):
        group = Group("group")

        self.assertFalse(is_user_in_group("invalid_sub_child_user", group))


if __name__ == "__main__":
    unittest.main()
