"""
Tic Tac Toe Player
"""

import math

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
    The player function should take a board state as input, and return which player's turn it is (either X or O).
    In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.
    Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).
    """
    x_count = 0
    o_count = 0
    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)

    if x_count > o_count:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_set.add((i, j))

    return actions_set

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")

    new_board = [[cell for cell in row] for row in board]

    i, j = action

    player_turn = player(board)

    new_board[i][j] = player_turn

    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O

    for j in range(3):
        if [board[i][j] for i in range(3)].count(X) == 3:
            return X
        elif [board[i][j] for i in range(3)].count(O) == 3:
            return O

    if [board[i][i] for i in range(3)].count(X) == 3 or \
       [board[i][2-i] for i in range(3)].count(X) == 3:
        return X
    elif [board[i][i] for i in range(3)].count(O) == 3 or \
         [board[i][2-i] for i in range(3)].count(O) == 3:
        return O

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or not any(EMPTY in row for row in board):
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)

    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    player_turn = player(board)

    optimal_move = None
    optimal_value = None

    if player_turn == X:
        optimal_value, optimal_move = max_value(board)
    else:
        optimal_value, optimal_move = min_value(board)

    return optimal_move

def max_value(board):
    """
    Utility function for maximizing player (X)
    Returns the maximum attainable value and the corresponding move
    """
    if terminal(board):
        return utility(board), None

    value = float('-inf')
    optimal_move = None

    for action in actions(board):
        new_value = min_value(result(board, action))[0]

        if new_value > value:
            value = new_value
            optimal_move = action

    return value, optimal_move

def min_value(board):
    """
    Utility function for minimizing player (O)
    Returns the minimum attainable value and the corresponding move
    """
    if terminal(board):
        return utility(board), None

    value = float('inf')
    optimal_move = None

    for action in actions(board):
        new_value = max_value(result(board, action))[0]

        if new_value < value:
            value = new_value
            optimal_move = action

    return value, optimal_move