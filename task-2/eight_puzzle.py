import copy


def initial_state():
    return ((7, 2, 4, 5, 0, 6, 8, 3, 1), 1, 1)


def is_goal(s):
    return s[0] == (1, 2, 3, 4, 5, 6, 7, 8, 0)


def successors(s):
    _, r, c = s
    new_r, new_c = r-1, c
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r+1, c
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r, c-1
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r, c+1
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1


def is_valid(r, c):
    return 0 <= r <= 2 and 0 <= c <= 2


def move_blank(s, new_r, new_c):
    board, r, c = s
    new_board = list(board)
    new_board[r*3 + c] = new_board[new_r*3 + new_c]
    new_board[new_r*3 + new_c] = 0
    return (tuple(new_board), new_r, new_c)

def h1(s):
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    board, _, _ = s
    res = 0
    # The for loop counts the number of elements that is different from
    # the goal configuration.
    # We start from index 1 to 8 because the blank is excluded.

    # Isn't it should be index 0 to 7 to check for number 1 to 8
    # because Python index start from 0?
    for idx in range(0, 8):
        if goal[idx] != board[idx]:
            res += 1
    return res

def h3(s):
    # implement this function
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    board, _, _ = s
    result = 0

    for idx in range(0, 9):
        if (board[idx] != 0):
            if ((board[idx]-1)//3 != (goal[idx]-1)//3): 
                # row diff
                result += 1
            if ((board[idx])%3 != goal[idx]%3): 
                # col diff
                result += 1

    return result
