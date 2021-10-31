import random
import tkinter
from tkinter import *
from tkinter.messagebox import showinfo


class SudokuUI(Frame):
    """
    Tkinter UI that will configure the user interface
    """

    def __init__(self, game_window, game):
        self.game = game
        Frame.__init__(self, game_window)
        self.game_window = game_window
        self.row, self.col = -1, -1
        self.__initUI()

    def __initUI(self):
        self.game_window.geometry('500x507')
        self.game_window.title('Sudoku')
        self.game_window.resizable(0, 0)
        self.__config_sudoku_frame()
        self.__config_game_buttons()

    def __config_sudoku_frame(self):
        self.sudoku_frame = Frame(self.game_window, bd=3, bg='black')
        self.sudoku_frame.pack(side=TOP)
        self.sudoku_cells = [[StringVar() for _ in range(9)] for _ in range(9)]
        self.entry_array = [[] for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if (r in (0, 1, 2, 6, 7, 8) and c in (0, 1, 2, 6, 7, 8)) or (r in (3, 4, 5) and c in (3, 4, 5)):
                    entry = tkinter.Entry(self.sudoku_frame, font=('arial', 23, 'bold'),
                                          textvariable=self.sudoku_cells[r][c], width=3,
                                          bg='#e6e6ff', bd=1, justify=CENTER,
                                          disabledbackground="#e6e6ff", disabledforeground="black")
                else:
                    entry = tkinter.Entry(self.sudoku_frame, font=('arial', 23, 'bold'),
                                          textvariable=self.sudoku_cells[r][c],
                                          width=3,
                                          bg='#ccccff', bd=1, justify=CENTER,
                                          disabledbackground="#ccccff", disabledforeground="black")
                self.sudoku_cells[r][c].trace("w", lambda *args: self.__character_limit(self.sudoku_cells))
                self.entry_array[r].append(entry)
                entry.grid(row=r, column=c)
        self.__show_the_board_on_GUI()

    @staticmethod
    def __character_limit(sudoku_cells):
        for r in range(9):
            for c in range(9):
                if len(sudoku_cells[r][c].get()) > 1:
                    sudoku_cells[r][c].set(sudoku_cells[r][c].get()[-1])
                if sudoku_cells[r][c].get() != '' and (not sudoku_cells[r][c].get().isdigit()
                                                       or sudoku_cells[r][c].get() == '0'):
                    sudoku_cells[r][c].set('')

    def __show_the_board_on_GUI(self):
        for r in range(9):
            for c in range(9):
                self.sudoku_cells[r][c].set('')
                self.entry_array[r][c].config(fg='black', state=DISABLED)
                if self.game.board[r][c] != '0':
                    self.sudoku_cells[r][c].set(self.game.board[r][c])
                else:
                    self.entry_array[r][c].config(fg='grey', state=NORMAL)

    def __config_game_buttons(self):
        self.buttons_frame = Frame(self.game_window, width=500, height=500, bg='black')
        self.buttons_frame.pack()
        self.submit_btn = Button(self.buttons_frame, text='Submit solution',
                                 font=('arial', 11),
                                 width=27, height=2, bg='#e6fff2', cursor='hand2',
                                 command=lambda: self.__check_solution()).grid(row=0, column=0)
        self.response_for_submit_text = StringVar()
        self.response_for_submit_label = Label(self.buttons_frame,
                                               textvariable=self.response_for_submit_text,
                                               font=('arial', 11),
                                               bg='white', bd=4.3,
                                               height=2, width=27)
        self.response_for_submit_label.grid(row=0, column=1)
        self.clear_btn = Button(self.buttons_frame, text='Clear',
                                font=('arial', 11),
                                width=27, height=2, bg='#ffe6e6', cursor='hand2',
                                command=lambda: self.__clear_board()).grid(row=2, column=1)
        self.check_btn = Button(self.buttons_frame, text='Check',
                                font=('arial', 11),
                                width=27, height=2, bg='#ffffe6', cursor='hand2',
                                command=lambda: self.__perform_check()).grid(row=1, column=1)
        self.generate_btn = Button(self.buttons_frame, text='Generate new sudoku',
                                   font=('arial', 11),
                                   width=27, height=2, bg='#e6fff2', cursor='hand2',
                                   command=lambda: self.__generate_a_new_board()).grid(row=2, column=0)
        self.solve_btn = Button(self.buttons_frame, text='Solve',
                                font=('arial', 11),
                                width=27, height=2, bg='#e6fff2', cursor='hand2',
                                command=lambda: self.__perform_solve()).grid(row=1, column=0)

    def __update_board_with_values_from_GUI(self):
        self.game.get_back_to_original_board()
        for r in range(9):
            for c in range(9):
                if self.game.board[r][c] == '0' and self.sudoku_cells[r][c].get() != '':
                    self.game.board[r][c] = self.sudoku_cells[r][c].get()

    def __check_solution(self):
        self.__update_board_with_values_from_GUI()
        if self.game.check_win() is True:
            showinfo('Result', 'Correct')
            self.response_for_submit_label.configure(fg='green')
            self.response_for_submit_text.set('Correct')
        else:
            showinfo('Result', 'Incorrect')
            self.response_for_submit_label.configure(fg='red')
            self.response_for_submit_text.set('Incorrect')
            self.__perform_check()

    def __clear_board(self):
        self.game.get_back_to_original_board()
        for r in range(9):
            for c in range(9):
                if self.game.board[r][c] == '0':
                    self.sudoku_cells[r][c].set('')
        self.__clear_red_squares()
        self.response_for_submit_text.set('')

    def __generate_a_new_board(self):
        self.game.get_a_new_board()
        self.__show_the_board_on_GUI()

    def __perform_check(self):
        self.__update_board_with_values_from_GUI()
        self.__clear_red_squares()
        duplicates_coordinates = self.game.search_for_duplicates()
        for element in duplicates_coordinates:
            self.entry_array[element[0]][element[1]].config(bg='pink')

    def __clear_red_squares(self):
        for r in range(9):
            for c in range(9):
                if (r in (0, 1, 2, 6, 7, 8) and c in (0, 1, 2, 6, 7, 8)) or (r in (3, 4, 5) and c in (3, 4, 5)):
                    self.entry_array[r][c].config(bg='#e6e6ff')
                else:
                    self.entry_array[r][c].config(bg='#ccccff')

    def __perform_solve(self):
        self.game.solve_sudoku()
        self.__update_GUI()

    def __update_GUI(self):
        for r in range(9):
            for c in range(9):
                self.sudoku_cells[r][c].set(self.game.board[r][c])


class GenerateSudokuBoard(object):
    """
    Will generate a board to play sudoku
    """

    def __init__(self):
        self.generated_board = []

    def generate_random_board(self):
        with open('boards.sudoku', 'r') as boards_file:
            board_number = random.randint(1, 50)
            searched_grid = 'Grid ' + str(board_number)
            read_rows = 0
            found_board = 0
            for line in boards_file:
                if searched_grid in line:
                    read_rows = 9
                    found_board = 1
                elif found_board and read_rows > 0:
                    self.generated_board.append(self.__get_row_as_list(line))
                    read_rows -= 1
                elif found_board and read_rows == 0:
                    break
            return self.generated_board

    @staticmethod
    def __get_row_as_list(line):
        row = line.strip()
        row_list = []
        for element in row:
            row_list.append(element)
        return row_list

    def generate_first_board(self):
        with open('boards.sudoku', 'r') as boards_file:
            lines = range(1, 10)
            for line in enumerate(boards_file):
                if line[0] in lines:
                    self.generated_board.append(self.__get_row_as_list(line[1]))
                if line[0] > 9:
                    break
        return self.generated_board


class SudokuGame(object):
    """
    This class will simulate the sudoku game,
    it will be used to hold the data about the board configuration
    and to check for wins or incorrect answers
    """

    def __init__(self):
        self.game_over = False
        self.board = None
        self.saved_copy_board = None
        self.solved_board = None

    def get_a_new_board(self):
        sudokuBoardGenerator = GenerateSudokuBoard()
        self.board = sudokuBoardGenerator.generate_random_board()
        self.saved_copy_board = self.__save_a_copy_board()
        self.solved_board = self.__save_a_copy_board()

    def __save_a_copy_board(self):
        copy_board = []
        for a_list in self.board:
            copy_board.append(list.copy(a_list))
        return copy_board

    def check_win(self):
        for row in range(9):
            if not self.__check_row(row):
                return False
        for column in range(9):
            if not self.__check_column(column):
                return False
        for row in range(3):
            for column in range(3):
                if not self.__check_square(row, column):
                    return False
        self.game_over = True
        return True

    @staticmethod
    def __check_block(block):
        return set(block) == {'8', '2', '9', '1', '6', '4', '3', '7', '5'}

    def __check_row(self, row):
        return self.__check_block(self.board[row])

    def __check_column(self, column):
        return self.__check_block(
            [self.board[row][column] for row in range(9)]
        )

    def __check_square(self, row, column):
        return self.__check_block(
            [
                self.board[r][c]
                for r in range(row * 3, (row + 1) * 3)
                for c in range(column * 3, (column + 1) * 3)
            ]
        )

    def search_for_duplicates(self):
        duplicates_coordinates = set()
        self.__search_for_duplicates_in_row(duplicates_coordinates)
        self.__search_for_duplicates_in_column(duplicates_coordinates)
        self.__search_for_duplicates_in_square(duplicates_coordinates)
        return duplicates_coordinates

    @staticmethod
    def __search_for_duplicates_in_block(block):
        duplicates_set = set([x for x in block if block.count(x) > 1])
        if duplicates_set.__contains__('0'):
            duplicates_set.remove('0')
        return duplicates_set

    def __search_for_duplicates_in_row(self, duplicates_coordinates):
        for row in range(9):
            duplicates = self.__search_for_duplicates_in_block(self.board[row])
            if duplicates != set():
                for element in range(9):
                    if self.board[row][element] in duplicates:
                        duplicates_coordinates.add((row, element))

    def __search_for_duplicates_in_column(self, duplicates_coordinates):
        for column in range(9):
            duplicates = self.__search_for_duplicates_in_block([self.board[row][column] for row in range(9)])
            if duplicates != set():
                for element in range(9):
                    if self.board[element][column] in duplicates:
                        duplicates_coordinates.add((element, column))

    def __search_for_duplicates_in_square(self, duplicates_coordinates):
        for row in range(3):
            for column in range(3):
                duplicates = self.__search_for_duplicates_in_block([
                    self.board[r][c]
                    for r in range(row * 3, (row + 1) * 3)
                    for c in range(column * 3, (column + 1) * 3)
                ])
                if duplicates != set():
                    for r in range(row * 3, (row + 1) * 3):
                        for c in range(column * 3, (column + 1) * 3):
                            if self.board[r][c] in duplicates:
                                duplicates_coordinates.add((r, c))

    def __validate(self, row, column, value):
        for i in range(9):
            if self.solved_board[row][i] == value:
                return False
        for i in range(9):
            if self.solved_board[i][column] == value:
                return False
        r0 = (row // 3) * 3
        c0 = (column // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.solved_board[r0 + i][c0 + j] == value:
                    return False
        return True

    def solve_sudoku(self):
        for r in range(9):
            for c in range(9):
                if self.solved_board[r][c] == '0':
                    for value in range(1, 10):
                        if self.__validate(r, c, str(value)):
                            self.solved_board[r][c] = str(value)
                            self.solve_sudoku()
                            self.solved_board[r][c] = '0'
                    return
        for r in range(9):
            for c in range(9):
                self.board[r][c] = self.solved_board[r][c]

    def get_back_to_original_board(self):
        for r in range(9):
            for c in range(9):
                self.board[r][c] = self.saved_copy_board[r][c]


if __name__ == '__main__':
    sudokuGame = SudokuGame()
    sudokuGame.get_a_new_board()
    window = Tk()
    SudokuUI(window, sudokuGame)
    window.mainloop()
