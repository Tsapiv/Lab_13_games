"""Module for running game"""

from Game_task_4.board import Board
from Game_task_4.tree import GameTree


def main():
    """
    Function for running game
    :return: str
    """
    board = Board()
    first_move = "x"
    while True:
        if not board.get_available():
            return "Draw"
        position = user_input()
        try:
            board.make_move(position, first_move)
        except IndexError:
            print("Invalid move")
            continue
        if board:
            print(board)
            print("==============")
        else:
            return "Draw"
        if board.status() == -1:
            return "You win"

        temp_tree = GameTree(board)
        temp_tree.build()
        board = temp_tree.best_move()
        if board:
            print(board)
            print("==============")
        else:
            return "Draw"
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
