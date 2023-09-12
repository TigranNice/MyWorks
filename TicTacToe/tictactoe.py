"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
        Returns player who has the next turn on a board.
        """
    count_x = 0
    count_y = 0
    for i in board:
        count_y += i.count(O)
        count_x += i.count(X)
    if count_x > count_y:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    st = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                st.add((i, j))
    return st


def result(board, action):
    board_action = deepcopy(board)
    board_action[action[0]][action[1]] = player(board)
    return board_action


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = None
    for i in board:
        if i.count(X) == 3:
            return X
        if i.count(O) == 3:
            return O

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == X:
            return X
        if board[0][i] == board[1][i] == board[2][i] == O:
            return O

    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    if board[0][2] == board[1][1] == board[2][0] == X:
        return X

    if board[0][0] == board[1][1] == board[2][2] == O:
        return O
    if board[0][2] == board[1][1] == board[2][0] == O:
        return O
    return winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    coun = 0
    for i in board:
        coun += i.count(X) + i.count(O)
    return winner(board) is not None or coun == 9


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win_score = winner(board)
    if win_score == X:
        return 1
    elif win_score == O:
        return -1
    return 0



def minimax(board, k = 0):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return utility(board)
    k += 1
    verities_of_actions = actions(board)
    sp = {}
    for i in verities_of_actions:
        res = minimax(result(board, i), k)
        if i in sp.keys():
            sp[i] += res
        else:
            sp[i] = res
    if k == 1:
        hod = None
        if player(board) == O:
            mini = 10_000
            for i in sp.keys():
                if sp[i] <= mini:
                    mini = sp[i]
                    hod = i
        else:
            maxi = -10_000
            for i in sp.keys():
                if sp[i] >= maxi:
                    maxi = sp[i]
                    hod = i
        return hod
    if player(board) == X:
        return max(sp.values())
    else:
        return min(sp.values())