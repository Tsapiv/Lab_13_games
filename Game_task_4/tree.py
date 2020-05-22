"""Module with game tree"""

from Game_task_4.node import Node


class GameTree:
    """Linked structure for creating game tree"""

    def __init__(self, start_board):
        """
        Create GameTree from Node
        :param start_board: Node
        """
        self._root = Node(start_board)

    def best_move(self):
        """
        Checks what branch is the best
        :return: Board
        """

        def recurse(node):
            """
            Recursive part itself
            :param node: Node
            :return: int
            """
            if not node.children:
                return node.data.status()
            else:
                return sum([recurse(child) for child in node.children])

        result = [recurse(child) for child in self._root.children]
        if result:
            points = max(result)
            return self._root.children[result.index(points)].data
        return

    def build(self):
        """
        Function for building GameTree recursively
        :return: None
        """

        def recurse(node):
            """
            The recursive part itself
            :param node: Node
            :return: None
            """
            next_moves = node.data.get_available()
            if next_moves:
                last_move = node.data.last_move
                next_turn = "x" if last_move != "x" else "0"
                for move in next_moves:
                    board = Node(node.data.copy())
                    board.data.make_move(move, next_turn)
                    node.children.append(board)
                    recurse(board)

        recurse(self._root)

    def get_root(self):
        """
        Returns root
        :return: GameNode
        """
        return self._root
