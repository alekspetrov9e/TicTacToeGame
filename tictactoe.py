"""
Tic Tac Toe Player
"""
import copy
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
    """
    if terminal(board):
        return X
    else:
        X_count = 0
        O_count = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == X:
                    X_count += 1
                elif board[i][j] == O:
                    O_count += 1
                else:
                    pass
        if X_count > O_count:
            return O
        else:
            return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None
    else:
        answer = set()
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    answer.add((i, j))

        return answer


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)
    if action not in actions(board_copy):
        raise Exception
    else:
        row = action[0]
        col = action[1]
        if player(board_copy) == X:
            board_copy[row][col] = X
        else:
            board_copy[row][col] = O
        return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (board[0][0] == X and board[0][1] == X and board[0][2] == X) or (
            board[1][0] == X and board[1][1] == X and board[1][2] == X) or (
            board[2][0] == X and board[2][1] == X and board[2][2] == X) or (
            board[0][0] == X and board[1][0] == X and board[2][0] == X) or (
            board[0][1] == X and board[1][1] == X and board[2][1] == X) or (
            board[0][2] == X and board[1][2] == X and board[2][2] == X) or (
            board[0][0] == X and board[1][1] == X and board[2][2] == X) or (
            board[0][2] == X and board[1][1] == X and board[2][0] == X):
        return X
    elif (board[0][0] == O and board[0][1] == O and board[0][2] == O) or (
            board[1][0] == O and board[1][1] == O and board[1][2] == O) or (
            board[2][0] == O and board[2][1] == O and board[2][2] == O) or (
            board[0][0] == O and board[1][0] == O and board[2][0] == O) or (
            board[0][1] == O and board[1][1] == O and board[2][1] == O) or (
            board[0][2] == O and board[1][2] == O and board[2][2] == O) or (
            board[0][0] == O and board[1][1] == O and board[2][2] == O) or (
            board[0][2] == O and board[1][1] == O and board[2][0] == O):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X:
        return True
    elif winner(board) == O:
        return True
    else:
        empty_count = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    empty_count += 1
        if empty_count == 0:
            return True
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    for action in actions(board):
        board_after_action = result(board, action)
        if terminal(board_after_action):
            return action

    for action in actions(board):
        if player(board) == X:
            if terminal(result2(board, action, O)):
                return action
        else:
            if terminal(result2(board, action, X)):
                return action

    actions_set = actions(board)
    return list(actions_set)[0]


def result2(board, move, pl):
    board_copy = copy.deepcopy(board)
    row = move[0]
    col = move[1]
    if pl == X:
        board_copy[row][col] = X
    else:
        board_copy[row][col] = O
    return board_copy

