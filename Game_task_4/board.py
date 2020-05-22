"""Module with board implementation"""

from copy import deepcopy


def sign(num):
    """
    Sign function
    :param num: number
    :return: int
    """
    if num < 0:
        return -1
    elif num > 0:
        return 1
    return 0


class Board:
    """Class for game board implementation"""

    def __init__(self):
        """
        Create empty board
        """
        self._field = [[None for _ in range(3)] for _ in range(3)]
        self.last_move = None

    def __str__(self):
        """
        Visual representation of board
        :return: str
        """
        board = ""
        for row in self._field:
            board += str([sign if sign is not None else " " for sign in row]) + "\n"
        return board.rstrip()

    def get_available(self):
        """
        Returns list of available positions
        :return: list
        """
        free_cells = []
        for j in range(3):
            for i in range(3):
                if self._field[j][i] is None:
                    free_cells.append((j, i))
        return free_cells

    def is_available(self, position):
        """
        Checks whether position is available
        :param position: list, tuple
        :return: bool
        """
        return self._field[position[0]][position[1]] is None

    def make_move(self, position, turn):
        """
        Make a move to given position
        :param turn: str
        :param position: list, tuple
        :return: None
        """
        self.last_move = turn
        if position[0] in range(3) and position[1] in range(3) and self.is_available(position):
            self._field[position[0]][position[1]] = turn
        else:
            raise IndexError

    def check_horizontal(self):
        """
        Check winning combination
        in rows
        :return: int
        """
        for row in range(3):
            if self._field[row][0] == self._field[row][1] == self._field[row][2] == "x":
                return -1
        for row in range(3):
            if self._field[row][0] == self._field[row][1] == self._field[row][2] == "0":
                return 1
        return 0

    def check_vertical(self):
        """
        Check winning combination
        in colons
        :return: int
        """
        for col in range(3):
            if self._field[0][col] == self._field[1][col] == self._field[2][col] == "x":
                return -1
        for col in range(3):
            if self._field[0][col] == self._field[1][col] == self._field[2][col] == "0":
                return 1
        return 0

    def check_cross(self):
        """
        Check winning combination
        in cross
        :return: int
        """
        if self._field[0][0] == self._field[1][1] == self._field[2][2] == "x":
            return -1
        elif self._field[2][0] == self._field[1][1] == self._field[0][2] == "x":
            return -1
        if self._field[0][0] == self._field[1][1] == self._field[2][2] == "0":
            return 1
        elif self._field[2][0] == self._field[1][1] == self._field[0][2] == "0":
            return 1
        return 0

    def status(self):
        """
        Get status of the game board
        If game continues, returns false
        :return: int
        """
        hor_res = self.check_horizontal()
        ver_res = self.check_vertical()
        cro_res = self.check_cross()
        return sign(hor_res + ver_res + cro_res)

    def set_field(self, field):
        """
        Returns field
        :param: field list(list)
        :return: None
        """
        self._field = field

    def copy(self):
        """
        Makes a copy of current board
        :return: Board
        """
        new_board = self.__class__()
        field = deepcopy(self._field)
        new_board.set_field(field)
        return new_board
