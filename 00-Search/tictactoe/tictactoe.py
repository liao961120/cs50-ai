"""
Tic Tac Toe Player
"""

#%%
import math
import itertools
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
    turns = 0
    for lst in board:
        for cell in lst:
            if cell is not EMPTY:
                turns += 1
    
    if turns % 2 == 0:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i, lst in enumerate(board):
        for j, cell in enumerate(lst):
            if cell is EMPTY:
                actions.add( (i, j) )
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result = deepcopy(board)

    if result[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid Action: cell not empty!")

    if player(board) == X:
        result[action[0]][action[1]] = X
    else:
        result[action[0]][action[1]] = O
    
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    def getUnitVec(p0, p1):
        x_diff = p1[0] - p0[0]
        y_diff = p1[1] - p0[1]
        # Make the direction of vector consistent
        if x_diff < 0:
            x_diff = -x_diff
            y_diff = -y_diff
        length = math.sqrt(x_diff**2 + y_diff**2)
        return ( x_diff/length, y_diff/length )

    # Get all coordinates of X and O
    X_coords = [(i, j) for i, lst in enumerate(board) for j, cell in enumerate(lst) if cell == X ]
    O_coords = [(i, j) for i, lst in enumerate(board) for j, cell in enumerate(lst) if cell == O ]

    # Return early if less than three
    if len(X_coords) < 3 and len(O_coords) < 3:
        return None
    
    # Get lines of all combinations of coords and check whether
    # the third cell fall on the line
    for t, coords in enumerate([X_coords, O_coords]):
        T = X if t == 0 else O
        for p0, p1 in itertools.combinations(coords, 2):
            unit_vec = getUnitVec(p0, p1)
            # Check whether third point is on the line
            for p2 in coords:
                if p2 == p0 or p2 == p1:
                    continue
                if all(math.isclose(a, b) for a, b in zip(getUnitVec(p0, p2), unit_vec)):
                    return T
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
