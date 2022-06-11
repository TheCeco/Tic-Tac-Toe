def read_players():
    player_one_name = input('Player one name: ')
    player_two_name = input('Player two name: ')

    player_one_symbol = input(f'{player_one_name} would you like to play with "X" or "0"? ').upper()
    while player_one_symbol not in ["X", "O"]:
        player_one_symbol = input(f'{player_one_name} would you like to play with "X" or "0"? ').upper()

    player_two_symbol = "0" if player_one_symbol == "X" else "X"
    return [(player_one_name, player_one_symbol), (player_two_name, player_two_symbol)]


def print_board_numeration(board):
    print("This is the numeration of the board:")
    idx = 1
    for row in range(len(board)):
        print("|", end='')
        for col in range(len(board)):
            print(f'  {idx}  |', end='')
            idx += 1
        print()


def get_position_mapping(board):
    result = {}
    idx = 1
    for row in range(len(board)):
        for col in range(len(board)):
            result[idx] = (row, col)
            idx += 1
    return result


def print_board(board):
    for row in range(len(board)):
        print("|", end='')
        for col in range(len(board)):
            print(f'  {" " if board[row][col] is None else board[row][col]}  |', end='')
        print()


def check_for_win(sign, player_row, player_col, board):
    # row
    won = True
    for col in range(len(board)):
        if board[player_row][col] != sign:
            won = False
            break
    if won:
        return True

    # col
    won = True
    for row in range(len(board)):
        if board[row][player_col] != sign:
            won = False
            break
    if won:
        return True

    # primary diagonal
    won = True
    for idx in range(len(board)):
        if board[idx][idx] != sign:
            won = False
            break
    if won:
        return True

    # secondary diagonal
    won = True
    for idx in range(len(board)):
        if board[idx][len(board) - 1 - idx] != sign:
            won = False
            break
    return won


def is_draw(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] is None:
                return False
    return True


def play_game(players, board, positions_mapping):
    print(f'{players[0][0]} starts first')
    while True:
        player_name, player_sign = players[0]
        position = input(f"{player_name} choose a free position [1-{len(board) * len(board)}]: ")
        if not position.isdigit():
            print(f'{position} is not a valid integer!')
            continue

        position = int(position)
        if position not in positions_mapping:
            print(f'{position} is not a valid position!')
            continue
            
        row, col = positions_mapping[position]
        if board[row][col] is not None:
            print(f'{position} is already selected!')
            continue
        
        board[row][col] = player_sign
        
        print_board(board)

        if check_for_win(player_sign, row, col, board):
            print(f'{player_name} won!')
            break

        if is_draw(board):
            print('DRAW!')
            break
        
        players[0], players[1] = players[1], players[0]


players = read_players()

board_size = 3
board = []
[board.append([None] * board_size) for _ in range(board_size)]

print_board_numeration(board)
positions_mapping = get_position_mapping(board)
play_game(players, board, positions_mapping)
