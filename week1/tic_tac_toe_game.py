turn_value = {0: 'X', 1: '0'}  # if turn is 0 then its X's turn, if turn is 1 then its 0's turn


def check_for_win(x_0_matrix):
    for i in range(0, 9, 3):  # check for rows
        if x_0_matrix[0 + i] == x_0_matrix[1 + i] and x_0_matrix[1 + i] == x_0_matrix[2 + i] \
                and x_0_matrix[0 + i] != ' ':
            return x_0_matrix[0 + i]

    for i in range(0, 2):  # check for columns
        if x_0_matrix[0 + i] == x_0_matrix[3 + i] and x_0_matrix[3 + i] == x_0_matrix[6 + i] \
                and x_0_matrix[0 + i] != ' ':
            return x_0_matrix[0 + i]

    # check for main diagonal
    if x_0_matrix[0] == x_0_matrix[4] and x_0_matrix[4] == x_0_matrix[8] and x_0_matrix[0] != ' ':
        return x_0_matrix[0]

    # check for the second diagonal
    if x_0_matrix[2] == x_0_matrix[4] and x_0_matrix[4] == x_0_matrix[6] and x_0_matrix[2] != ' ':
        return x_0_matrix[2]
    # if no win found then
    return None


def check_for_end_of_game(fields_filled, x_0_matrix):
    winner = check_for_win(x_0_matrix)
    game_finished = 0
    if winner is not None:
        game_finished = 1
    elif fields_filled >= 9:
        game_finished = 1
    return winner, game_finished


def print_matrix(x_0_matrix):
    print("""
             {} | {} | {}            1 | 2 | 3 
            ---|---|---          ---|---|---
             {} | {} | {}            4 | 5 | 6 
            ---|---|---          ---|---|---
             {} | {} | {}            7 | 8 | 9
            """.format(x_0_matrix[0], x_0_matrix[1], x_0_matrix[2],
                       x_0_matrix[3], x_0_matrix[4], x_0_matrix[5],
                       x_0_matrix[6], x_0_matrix[7], x_0_matrix[8]))


def computer_make_move(value, x_0_matrix):
    # try first to place in 5 position
    if x_0_matrix[4] == ' ':
        x_0_matrix[4] = value

    # else the choices are 1, 3, 7, 9 positions in order
    elif x_0_matrix[0] == ' ' or x_0_matrix[2] == ' ' or x_0_matrix[6] == ' ' or x_0_matrix[8] == ' ':
        if x_0_matrix[0] == ' ':
            x_0_matrix[0] = value
        elif x_0_matrix[2] == ' ':
            x_0_matrix[2] = value
        elif x_0_matrix[6] == ' ':
            x_0_matrix[6] = value
        else:
            x_0_matrix[8] = value

    # else the choices are 2, 4, 6, 8 positions in order
    elif x_0_matrix[1] == ' ' or x_0_matrix[3] == ' ' or x_0_matrix[5] == ' ' or x_0_matrix[7] == ' ':
        if x_0_matrix[1] == ' ':
            x_0_matrix[1] = value
        elif x_0_matrix[3] == ' ':
            x_0_matrix[3] = value
        elif x_0_matrix[5] == ' ':
            x_0_matrix[5] = value
        else:
            x_0_matrix[7] = value
    return 0


def player_make_move(value, x_0_matrix):
    place = input(f"Select a place for {value} in range [1, 9]: ")
    if x_0_matrix[int(place) - 1] == ' ':
        x_0_matrix[int(place) - 1] = value
        return 0
    return 1


def make_move(current_turn_value, player_chosen_value, x_0_matrix):
    if player_chosen_value == current_turn_value:
        ret_val = player_make_move(current_turn_value, x_0_matrix)
        if ret_val != 0:
            print("Incorrect place")
            return 1
    else:
        print("Computer is making move...")
        ret_val = computer_make_move(current_turn_value, x_0_matrix)
    return ret_val


def change_turn(current_turn):
    if current_turn == 0:
        current_turn = 1
    else:
        current_turn = 0
    return current_turn


def start_game():
    print("GAME STARTS")
    x_0_matrix = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    winner = None
    game_finished = 0
    turn = 0  # initialize turn on 0, as X starts first
    fields_filled = 0
    player_chosen_value = input("What do you want to play? X or 0? ")
    if player_chosen_value != 'X' and player_chosen_value != '0':
        print("Incorrect value")
    else:
        if player_chosen_value == '0':
            computer_make_move('X', x_0_matrix)
            turn = 1
            fields_filled += 1

        while not game_finished:
            print_matrix(x_0_matrix)
            # make the next move based on turn and the player chosen value
            if make_move(turn_value.get(turn), player_chosen_value, x_0_matrix) != 0:
                continue  # if move could not be made go to next loop, without changing turn
            turn = change_turn(turn)
            fields_filled += 1
            winner, game_finished = check_for_end_of_game(fields_filled, x_0_matrix)

        print_matrix(x_0_matrix)
        if winner is None:
            print("Tie!")
        else:
            print(f"{winner} wins!")
    print("GAME OVER")


if __name__ == '__main__':
    start_game()
