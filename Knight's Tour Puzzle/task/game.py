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


def print_matrix(board_mtx, num_sep, print_type):
    if print_type == 1:
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
    elif print_type == 2:
        for i in range(len(board_mtx), 0, -1):
            str_row = ''
            for j in range(0, len(board_mtx[i - 1])):
                str_row = str_row + ' ' + ' ' * (len(str(max(board_mtx[i - 1]))) - len(str(board_mtx[i - 1][j]))) + str(board_mtx[i - 1][j])
            print(' ' * (len(str(len(board_mtx[i - 1]))) - len(str(i))), str(i), '|', str_row, ' |', sep="")



def print_desc(board_val, board_mtx, num_sep, print_type):
    print(' ' * len(str(board_val[1])), '-' * (board_val[0] * (num_sep + 1) + 3), sep='')
    print_matrix(board_mtx, num_sep, print_type)
    footer = range(1, board_val[0] + 1)
    print(' ' * len(str(board_val[1])), '-' * (board_val[0] * (num_sep + 1) + 3), sep='')
    print(' ' * (len(str(board_val[1])) + 1), ''.join(' ' * ((num_sep + 1) - len(str(x))) + str(x) for x in footer), sep='')


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
    game_over_result = 0
    count_move = [j for i in input_board_mtx for j in i if str(j).isdigit()]
    count_not_visited = [j for i in input_board_mtx for j in i if j == 'o']
    count_visited = [j for i in input_board_mtx for j in i if str(j) in ['*', 'X']]
    # print("count_move = ", count_move)
    # print("count_not_visited = ", count_not_visited)
    # print("count_visited = ", count_visited)
    if len(count_move) == 0:
        if len(count_not_visited) == 0:
            game_over_status = 'What a great tour! Congratulations!'
            game_over_result = 1
        else:
            game_over_status = 'No more possible moves!' + '\n\r' + 'Your knight visited {0} squares!'.format(len(count_visited))
    return game_over_status, game_over_result


def change_desk(board_mtx, position_val, board_val, num_sep, is_print_desk):
    # print(' ' * len(str(board_val[1])), '-' * (board_val[0] * (num_sep + 1) + 3), sep='')
    board_mtx = [['*' if x == 'X' else x for x in l] for l in board_mtx]
    board_mtx = [['o' if str(x).isdigit() else x for x in l] for l in board_mtx]
    board_mtx[position_val[1]-1][position_val[0]-1] = 'X'
    for offset in offset_list:
        board_mtx = get_possible_step(board_mtx, position_val, 0, 1, offset)

    if is_print_desk:
        print_desc(board_val, board_mtx, num_sep, 1)
        # print(' ' * len(str(board_val[1])), '-' * (board_val[0] * (num_sep + 1) + 3), sep='')
        # print_matrix(board_mtx, num_sep)
        # footer = range(1, board_val[0] + 1)
        # print(' ' * len(str(board_val[1])), '-' * (board_val[0] * (num_sep + 1) + 3), sep='')
        # print(' ' * (len(str(board_val[1])) + 1), ''.join(' ' * ((num_sep + 1) - len(str(x))) + str(x) for x in footer), sep='')
    game_over_status, game_result = check_is_game_over(board_mtx)
    return board_mtx, game_over_status, game_result


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


def get_input_position(board_size, input_is_first, input_board_mtx, is_corrcet_move):
    while True:
        try:
            start_txt = "Enter the knight's starting position: "
            next_move_txt = "Enter your next move:"
            invalid_move = "Invalid move!"
            next_move_txt = next_move_txt if is_corrcet_move else invalid_move + " " + next_move_txt
            input_position = list(map(int, input(start_txt if input_is_first else next_move_txt).split(" ")))
            if len(input_position) >= num_dim:
                if input_position[0] in range(board_size[0], 0, -1) and input_position[1] in range(board_size[1], 0, -1):
                    if check_is_position_visited(input_position, input_board_mtx) == 0:
                        if input_is_first:
                            is_corrcet_move = True
                            break
                        elif check_is_possible_step(input_position, input_board_mtx) == 1:
                            is_corrcet_move = True
                            break
                        else:
                            # print("Invalid move!")
                            is_corrcet_move = False
                    else:
                        print("Invalid move!")
                        is_corrcet_move = False
                else:
                    print("Invalid position!")
            else:
                print("Invalid position!")
        except ValueError:
            print("Invalid position!")
    return input_position, is_corrcet_move


def is_exist_solution(board_mtx, board, num_sep, game_over, solution_list):
    board_mtx_tmp, game_over_tmp, game_result_tmp, solution_list_tmp = find_solution(board_mtx, board, num_sep, game_over, 0, solution_list)
    return game_result_tmp


def print_solution(input_board_mtx, input_solution_list, num_sep, axis_x, axis_y, board):
    for i, solution in enumerate(input_solution_list):
        input_board_mtx[solution[axis_x] - 1][solution[axis_y] - 1] = i + 1
    # print(input_board_mtx)
    print_desc(board, board_mtx, num_sep, 2)


def get_max_possible_position(mtx):
    max_val = min([x if str(x).isdigit() else 1000 for l in mtx  for x in l])
    if set([x for l in mtx for x in l]) == set('o'):
        pos = (1, len(mtx))
    else:
        pos = [[(j, i) for j, x in enumerate(l) if str(x).isdigit() and x == max_val] for i, l in enumerate(mtx)]
        pos = [x for x in pos if len(x) > 0][0][0]
        pos = tuple(map(lambda x: x + 1, pos))
    return pos


def find_solution(board_mtx, board, num_sep, game_over, game_result, solution_list):
    # game_result = 0
    if game_over:
        return board_mtx, game_over, game_result, solution_list
    else:
        calc_position = get_max_possible_position(board_mtx)
        # print(calc_position)
        solution_list.append(calc_position)
        board_mtx, game_over, game_result = change_desk(board_mtx, calc_position, board, num_sep, is_print_desk=False)
        # print("game_result = ", game_result)
        return find_solution(board_mtx, board, num_sep, game_over, game_result, solution_list)


num_dim = 2
min_board = 3
steps_list = [1, 2, -1, -2]
is_first = True
offset_list = [(steps_list[i], steps_list[j]) for i in range(len(steps_list)) for j in range(len(steps_list)) if abs(steps_list[i]) != abs(steps_list[j])]
board = get_input_board_size()
num_sep = len(str(board[0])) + 1
board_mtx = [['o' for i in range(0, board[0])] for j in range(0, board[1])]
solution_list = []
while True:
    game_over = False
    is_corrcet_move = True
    position, is_corrcet_move = get_input_position(board, is_first, board_mtx, is_corrcet_move)
    type_game = input("Do you want to try the puzzle? (y/n):")
    if type_game == 'y':
        if is_exist_solution(board_mtx, board, num_sep, game_over, solution_list) == 1:
            while not game_over:
                # print("is_first = ", is_first)
                if not is_first:
                    position, is_corrcet_move = get_input_position(board, is_first, board_mtx, is_corrcet_move)
                is_first = False
                solution_list.append(position)
                board_mtx, game_over, game_result = change_desk(board_mtx, position, board, num_sep, True)
            print(game_over)
        else:
            print('No solution exists!')
        break
    elif type_game == 'n':
        board_mtx, game_over, result, solution_list = find_solution(board_mtx, board, num_sep, game_over, 0, solution_list)
        # print("game_over = ", game_over)
        # print("game_result = ", result)
        # print("solution_list = ", solution_list)
        if result == 1:
            print("Here's the solution!")
            print_solution(board_mtx, solution_list, num_sep, 1, 0, board)
        else:
            print('No solution exists!')
        break
    else:
        print('Invalid input!')



