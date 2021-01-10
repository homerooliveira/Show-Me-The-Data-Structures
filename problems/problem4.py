from typing import List, final

@final
class Group:
    name: str
    groups: List['Group']
    users: List[str]

    def __init__(self, _name: str):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group: 'Group'):
        self.groups.append(group)

    def add_user(self, user: str):
        self.users.append(user)

    def get_groups(self) -> List['Group']:
        return self.groups

    def get_users(self) -> List[str]:
        return self.users

    def get_name(self) -> str:
        return self.name

def is_user_in_group(user: str, group: Group) -> bool:
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    for user_name in group.users:
        if user == user_name:
            return True

    for g in group.groups:
        if is_user_in_group(user, g):
            return True

    return False
    
if __name__ == "__main__":
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group("t", parent))