"""Module for node instance"""


class GameNode:
    """Represents a node for a linked binary search tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def get_data(self):
        """
        Returns data
        :return: object
        """
        return self.data
