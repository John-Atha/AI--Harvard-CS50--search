# Tic Tac Toe Player

'''
Two optimizations found.
One can be used each time.
1) Alpha-beta pruning
2) Keep a set of explored boards and two hashmaps with their values and suggested actions,
in order not to repeat the same calculations
'''

# opt = 0 # for alpha-beta
opt = 1 # for explored and hashmaps solution


X = "X"
O = "O"
EMPTY = None

# Returns player who has the next turn on a board.
def player(board):
    countX = 0
    countO = 0
    for line in board:
        for cell in line:
            if cell == X:
                countX += 1
            elif cell == O:
                countO += 1
    return X if countX <= countO else O

# Returns set of all possible actions (i, j) available on the board.
def actions(board):
    res = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                res.add((i, j))
    return res

# Returns the board that results from making move (i, j) on the board.
def result(board, action):
    i, j = action
    if board[i][j]:
        raise Exception('Invalid action')
    newBoard = [line.copy() for line in board]
    pl = player(board)
    newBoard[i][j] = pl
    return newBoard

# Returns the winner of the game, if there is one.
def winner(board):
    def row_winner(index):
        row = board[index]
        if row[0] == row[1] == row[2] != None:
            return row[0]
        return False

    def column_winner(index):
        if board[0][index] == board[1][index] == board[2][index] != None:
            return board[0][index]
        return False

    def diag_winner():
        if board[0][0] == board[1][1] == board[2][2] != None or board[0][2] == board[1][1] == board[2][0] != None:
            return board[1][1]
        return False

    for i in range(3):
        if row_winner(i):
            return row_winner(i)
        if column_winner(i):
            return column_winner(i)

    return diag_winner() if diag_winner() else None

# Returns True if the table is full
def full(board):
    for line in board:
        for cell in line:
            if not cell:
                return False
    return True

# Returns True if game is over, False otherwise.
def terminal(board):
    return winner(board) or full(board)

# Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
def utility(board):
    return 1 if winner(board) == X else (-1 if winner(board) == O else 0)

class State():
    def __init__(self, board):
        self.board = board
        self.turn = player(board)
        self.value = -2 if self.turn == X else +2
        self.actions = actions(board)
        self.terminal = terminal(board)
        self.utility = utility(board)
        self.action = None

# Returns starting state of the board.
def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

# Turns board from list to string
# to use it in the explored set and as dictionaries key
def board_to_str(board):
    board2 = [list(map(lambda n: ' ' if n is None else n, line)) for line in board]
    return(','.join(board2[0])+','+','.join(board2[1])+','+','.join(board2[2]))

def maxvalue(board, explored = set(), value_dict = {}, action_dict = {}, parent = None):
    state = State(board = board)
    if state.terminal:
        return state.utility
    # opt with hashmaps
    if opt and board_to_str(board) in explored:
        state.value = value_dict[board_to_str(board)]
        state.action = action_dict[board_to_str(board)]
        return state
    for action in state.actions:
        mini = minvalue(result(state.board, action), explored = explored, value_dict = value_dict, action_dict = action_dict, parent = parent)
        if not type(mini)==int:
            mini = mini.value
        if mini >= state.value:
            state.action = action
            state.value = mini
        # alpha-beta pruning
        if not opt and parent is not None and mini > parent.value:
            break
    # opt with hashmaps
    if opt:
        explored.add(board_to_str(board))
        value_dict[board_to_str(board)] = state.value
        action_dict[board_to_str(board)] = state.action
    return state

def minvalue(board, explored = set(), value_dict = {}, action_dict = {}, parent = None):
    state = State(board = board)
    if state.terminal:
        return state.utility
    # opt with hashmaps
    if opt and board_to_str(board) in explored:
        state.value = value_dict[board_to_str(board)]
        state.action = action_dict[board_to_str(board)]
        return state
    for action in state.actions:
        maxi = maxvalue(result(state.board, action), explored = explored, value_dict = value_dict, action_dict = action_dict, parent = parent)
        if not type(maxi)==int:
            maxi = maxi.value
        if maxi <= state.value:
            state.action = action
            state.value = maxi
        # alpha-beta pruning
        if not opt and parent is not None and maxi < parent.value:
            break
        # opt with hashmaps
        if opt:
            explored.add(board_to_str(board))
            value_dict[board_to_str(board)] = state.value
            action_dict[board_to_str(board)] = state.action
    return state

# Returns the optimal action for the current player on the board.
def minimax(board):
    # opt with hashmaps
    explored = set()
    value_dict = {}
    action_dict = {}
    state = State(board = board)
    if state.terminal:
        return None
    # max player
    if state.turn == X:
        child = maxvalue(board, explored = explored, value_dict = value_dict, action_dict = action_dict)
        return child.action
    # min player
    child = minvalue(board, explored = explored, value_dict = value_dict, action_dict = action_dict)
    return child.action

def print_board(board):
    print(board[0], board[1], board[2], sep='\n')