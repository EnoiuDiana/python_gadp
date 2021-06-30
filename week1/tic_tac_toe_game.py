x_0_matrix = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
game_finished = 0
fields_filled = 0
turn_value = {0: 'X', 1: '0'}  # if turn is 0 then its X's turn, if turn is 1 then its 0's turn
turn = 0  # initialize turn on 0, as X starts first
winner = None
player_chosen_value = None


def check_for_win():
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

    return None


def print_matrix():
    print("""
             {} | {} | {}            1 | 2 | 3 
            ---|---|---          ---|---|---
             {} | {} | {}            4 | 5 | 6 
            ---|---|---          ---|---|---
             {} | {} | {}            7 | 8 | 9
            """.format(x_0_matrix[0], x_0_matrix[1], x_0_matrix[2],
                       x_0_matrix[3], x_0_matrix[4], x_0_matrix[5],
                       x_0_matrix[6], x_0_matrix[7], x_0_matrix[8]))


def computer_make_move(value):
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


def player_make_move(value):
    place = input(f"Select a place for {value} in range [1, 9]: ")
    if x_0_matrix[int(place) - 1] == ' ':
        x_0_matrix[int(place) - 1] = value
        return 0
    return 1


def make_move(value):
    if player_chosen_value == value:
        if player_make_move(value) != 0:
            print("Incorrect place")
            return 1
    else:
        print("Computer is making move...")
        computer_make_move(value)
    return 0


def change_turn():
    global turn
    if turn == 0:
        turn = 1
    else:
        turn = 0


def check_for_end_of_game():
    global winner, game_finished
    winner = check_for_win()
    if winner is not None:
        game_finished = 1
    elif fields_filled >= 9:
        game_finished = 1


def start_game():
    global game_finished, turn, fields_filled, winner

    print("GAME STARTS")
    while not game_finished:
        print_matrix()
        if make_move(turn_value.get(turn)) != 0:  # make the next move based on turn
            continue  # if move could not be made go to next loop, without changing turn
        change_turn()
        fields_filled += 1
        check_for_end_of_game()

    print_matrix()
    print(f"{winner} wins!")
    print("GAME OVER")


if __name__ == '__main__':
    player_chosen_value = input("What do you want to play? X or 0? ")
    if player_chosen_value == '0':
        computer_make_move('X')
        turn = 1
        fields_filled += 1
        start_game()
    elif player_chosen_value == 'X':
        start_game()
    else:
        print("Incorrect value")
