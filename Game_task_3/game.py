"""Module for running game"""

from Game_task_3.board import Board
from Game_task_3.btree import GameTree


def main():
    """
    Function for running game
    :return: str
    """
    board = Board()
    first_move = "x"
    while True:
        if not board.get_available():
            return "Done"
        position = user_input()
        try:
            board.make_move(position, first_move)
        except IndexError:
            print("Invalid move")
            continue
        print(board)
        print("==============")
        if board.status() == -1:
            return "You win"

        temp_tree = GameTree(board)
        temp_tree.build()
        if temp_tree.is_left_better():
            board = temp_tree.get_root().left.data
        else:
            board = temp_tree.get_root().right.data
        print(board)
        print("==============")
        if board.status() == 1:
            return "Machine wins"


def user_input():
    """
    Function for getting user input
    :return: tuple
    """
    move = input("Your turn: ")
    try:
        move = list(map(int, move.split()))
        position = (move[0], move[1])
    except (ValueError, IndexError):
        print("Invalid input!")
        return user_input()
    return position


if __name__ == '__main__':
    print(main())
