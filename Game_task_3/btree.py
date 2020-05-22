"""Module with game tree"""

import random
from Game_task_3.btnode import GameNode


class GameTree:
    """Linked structure for creating game tree"""

    def __init__(self, start_board):
        """
        Create GameTree from Board
        :param start_board: Board
        """
        self._root = GameNode(start_board)

    def is_left_better(self):
        """
        Checks whether left branch is better
        to continue with
        :return: bool
        """

        def recurse(node):
            if node is None:
                return 0
            elif node.left is None and node.right is None:
                return node.data.status()
            else:
                return recurse(node.left) + recurse(node.right)

        left = recurse(self._root.left)
        right = recurse(self._root.right)
        if left >= right:
            return True
        return False

    def build(self):
        """
        Function for building GameTree recursively
        :return: None
        """

        def recurse(node):
            """
            The recursive part itself
            :param node: GameNode
            :return: None
            """
            if node.data.get_available():
                last_move = node.data.last_move
                next_turn = "x" if last_move != "x" else "0"
                try:
                    next_moves = random.sample(node.data.get_available(), 2)
                except ValueError:
                    left_board = GameNode(node.data.copy())
                    left_board.data.make_move(node.data.get_available()[0], next_turn)
                    node.left = left_board
                    recurse(left_board)
                else:
                    right_board = GameNode(node.data.copy())
                    left_board = GameNode(node.data.copy())
                    right_board.data.make_move(next_moves[0], next_turn)
                    left_board.data.make_move(next_moves[1], next_turn)
                    node.right = right_board
                    node.left = left_board
                    recurse(right_board)
                    recurse(left_board)

        recurse(self._root)

    def get_root(self):
        """
        Returns root
        :return: GameNode
        """
        return self._root
