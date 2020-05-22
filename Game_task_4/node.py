"""Module for node instance"""


class Node:
    """Represents a node for a linked binary search tree."""

    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)

    def get_data(self):
        """
        Returns data
        :return: object
        """
        return self.data
