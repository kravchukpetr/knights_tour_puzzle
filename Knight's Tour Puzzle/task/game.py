# Write your code here

def get_possible_step(board_mtx, position_val, axis_x, axis_y, offset):
    offset_x = offset[axis_x]
    offset_y = offset[axis_y]
    position_val_y = position_val[axis_y] - 1
    position_val_x = position_val[axis_x] - 1
    if 0 <= position_val_y + offset_y < len(board_mtx):
        if 0 <= position_val_x + offset_x < len(board_mtx[position_val_y + offset_y]):
            if board_mtx[position_val_y + offset_y][position_val_x + offset_x] not in ['*', 'X']:
                count_ways = get_count_ways(board_mtx, [position_val_x + offset_x, position_val_y + offset_y], axis_x, axis_y)
                board_mtx[position_val_y + offset_y][position_val_x + offset_x] = count_ways
    return board_mtx


def print_matrix(board_mtx, num_sep):
    for i in range(len(board_mtx), 0, -1):
        str_row = ''
        for j in range(0, len(board_mtx[i - 1])):
            if board_mtx[i - 1][j] in ['X', '*']:
                str_row = str_row + ' ' * num_sep + board_mtx[i - 1][j]
            elif str(board_mtx[i - 1][j]).isdigit() and board_mtx[i - 1][j] >= 0:
                str_row = str_row + ' ' * num_sep + str(board_mtx[i - 1][j])
            else:
                str_row = str_row + ' ' + '_' * num_sep
        print(' ' * (len(str(len(board_mtx[i - 1]))) - len(str(i))), str(i), '|', str_row, ' |', sep="")


def get_count_ways(board_mtx, position_val, axis_x, axis_y):
    count_ways = 0
    position_val_y = position_val[axis_y]
    position_val_x = position_val[axis_x]
    for offset in offset_list:
        offset_x = offset[axis_x]
        offset_y = offset[axis_y]
        if 0 <= position_val_y + offset_y < len(board_mtx):
            if 0 <= position_val_x + offset_x < len(board_mtx[position_val_y + offset_y]):
                if board_mtx[position_val_y + offset_y][position_val_x + offset_x] not in ['X', '*']:
                    count_ways += 1
    return count_ways


def check_is_game_over(input_board_mtx):
    game_over_status = False
    count_move = [j for i in input_board_mtx for j in i if str(j).isdigit()]
    count_not_visited = [j for i in input_board_mtx for j in i if j == 'o']
    count_visited = [j for i in input_board_mtx for j in i if str(j) in ['*', 'X']]
    if len(count_move) == 0:
        if len(count_not_visited) == 0:
            game_over_status = 'What a great tour! Congratulations!'
        else:
            game_over_status = 'No more possible moves!' + '\n\r' + 'Your knight visited {0} squares!'.format(len(count_visited))
    return game_over_status


def print_desk(board_mtx, position_val, board_val):
    num_sep = len(str(board_val[0])) + 1
    print(' ' * len(str(board_val[1])), '-' * (board_val[0] * (num_sep + 1) + 3), sep='')
    board_mtx = [['*' if x == 'X' else x for x in l] for l in board_mtx]
    board_mtx = [['o' if str(x).isdigit() else x for x in l] for l in board_mtx]
    board_mtx[position_val[1]-1][position_val[0]-1] = 'X'
    for offset in offset_list:
        board_mtx = get_possible_step(board_mtx, position_val, 0, 1, offset)

    print_matrix(board_mtx, num_sep)
    footer = range(1, board_val[0] + 1)
    print(' ' * len(str(board_val[1])), '-' * (board_val[0] * (num_sep + 1) + 3), sep='')
    print(' ' * (len(str(board_val[1])) + 1), ''.join(' ' * ((num_sep + 1) - len(str(x))) + str(x) for x in footer), sep='')
    game_over_status = check_is_game_over(board_mtx)
    return board_mtx, game_over_status


def check_is_position_visited(position_val, matrix):
    if matrix[position_val[1] - 1][position_val[0] - 1] in ['X', '*']:
        return 1
    else:
        return 0


def check_is_possible_step(position_val, matrix):
    if str(matrix[position_val[1] - 1][position_val[0] - 1]).isdigit():
        if matrix[position_val[1] - 1][position_val[0] - 1] >= 0:
            return 1
        else:
            return 0
    else:
        return 0


def get_input_board_size():
    while True:
        try:
            board_size = list(map(int, input("Enter your board dimensions: ").split(" ")))
            if min(board_size) < min_board or len(board_size) < num_dim:
                print("Invalid dimensions!")
            else:
                break
        except ValueError:
            print("Invalid dimensions!")
    return board_size


def get_input_position(board_size, input_is_first, input_board_mtx):
    while True:
        try:
            start_txt = "Enter the knight's starting position: "
            next_move_txt = "Enter your next move:"
            input_position = list(map(int, input(start_txt if input_is_first == 1 else next_move_txt).split(" ")))
            if len(input_position) >= num_dim:
                if input_position[0] in range(board_size[0], 0, -1) and input_position[1] in range(board_size[1], 0, -1):
                    if check_is_position_visited(input_position, input_board_mtx) == 0:
                        if input_is_first == 1:
                            input_is_first = 0
                            break
                        elif check_is_possible_step(input_position, input_board_mtx) == 1:
                            break
                        else:
                            print("Invalid move!")
                    else:
                        print("Invalid move!")
                else:
                    print("Invalid position!")
            else:
                print("Invalid position!")
        except ValueError:
            print("Invalid position!")
    return input_position, input_is_first


num_dim = 2
min_board = 0
steps_list = [1, 2, -1, -2]
is_first = 1
game_over = False
offset_list = [(steps_list[i], steps_list[j]) for i in range(len(steps_list)) for j in range(len(steps_list)) if abs(steps_list[i]) != abs(steps_list[j])]
board = get_input_board_size()
board_mtx = [['o' for i in range(0, board[0])] for j in range(0, board[1])]
while not game_over:
    position, is_first = get_input_position(board, is_first, board_mtx)
    board_mtx, game_over = print_desk(board_mtx, position, board)
print(game_over)
