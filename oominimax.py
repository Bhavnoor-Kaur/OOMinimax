# -------------------------------------------------------
# Name: Bhavnoor Kaur
# Student ID: 1623727
# CMPUT 274, Fall 2020
#
# Weekly Assignment 6: OO Minimax
# -------------------------------------------------------
from math import inf as infinity
from random import choice
from random import seed as randomseed    
import platform
import time
from os import system

"""
An implementation of Minimax AI Algorithm in Tic Tac Toe,
using Python.
This software is available under GPL license.
Author: Clederson Cruz
Year: 2017
License: GNU GENERAL PUBLIC LICENSE (GPL)

Bhavnoor Kaur
CCID: bkaur
"""
# Setting the variable values of HUMAN and COMP players
HUMAN = -1
COMP = +1

class State:

    """
    This Class sets the move by validating the move considering the empty cells remaining at
    each point in the game, it also renders the board and prints it out to the terminal
    """
    # initialising all the variables
    def __init__(self, c_choice, h_choice, state = [[0,0,0], [0,0,0], [0,0,0]]):
        self.c_choice = c_choice
        self.h_choice = h_choice
        self.state = state
        self.chars = {}
        self.player = -2
        self.cells = []
        self.x = -1
        self.y = -1

    def __str__(self):
        return ("The human choice for this game is "
        + self.h_choice.upper() + " and the computer choice is " + self.c_choice.upper()
        )

    def __repr__(self):
        return self.state

    def get_c_choice(self):
        return self.c_choice

    def get_h_choice(self):
        return self.h_choice

    def get_state(self):
        return self.state

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def render(self, c_choice, h_choice):
        """
        Print the board on console
        param: c_choice - computer choice
               h_choice - human choice
        
        returns: None
        """
        self.chars = {
            -1: self.h_choice,
            +1: self.c_choice,
            0: ' '
        }
        str_line = '---------------'

        print('\n' + str_line)
        for row in self.state:
            for cell in row:
                symbol = self.chars[cell]
                print(f'| {symbol} |', end='')
            print('\n' + str_line)

    def wins(self, player):
            """
            This function tests if a specific player wins. Possibilities:
            * Three rows    [X X X] or [O O O]
            * Three cols    [X X X] or [O O O]
            * Two diagonals [X X X] or [O O O]
            :param player: a human or a computer
            :return: True if the player wins
            """
            self.player = player

            win_state = [
                [self.state[0][0], self.state[0][1], self.state[0][2]],
                [self.state[1][0], self.state[1][1], self.state[1][2]],
                [self.state[2][0], self.state[2][1], self.state[2][2]],
                [self.state[0][0], self.state[1][0], self.state[2][0]],
                [self.state[0][1], self.state[1][1], self.state[2][1]],
                [self.state[0][2], self.state[1][2], self.state[2][2]],
                [self.state[0][0], self.state[1][1], self.state[2][2]],
                [self.state[2][0], self.state[1][1], self.state[0][2]],
            ]
            if [self.player, self.player, self.player] in win_state:
                return True
            else:
                return False

    def evaluate(self):
        """
        Function to heuristic evaluation of state.
        :return: +1 if the computer wins; -1 if the human wins; 0 draw
        """
        if self.wins(COMP):
            score = +1
        elif self.wins(HUMAN):
            score = -1
        else:
            score = 0

        return score


    def game_over(self):
        """
        This function test if the human or computer wins
        :return: True if the human or computer wins
        """
        return self.wins(HUMAN) or self.wins(COMP)


    def empty_cells(self):
        """
        Each empty cell will be added into cells' list
        :return: a list of empty cells
            """
        self.cells = []

        for x, row in enumerate(self.state):
            for y, cell in enumerate(row):
                if cell == 0:
                    self.cells.append([x, y])

        return self.cells

    def get_depth(self):
        """
        This function returns the depth of the board at
        any time, i.e the length of empty cells list
        """
        return len(self.empty_cells())

    def valid_move(self, x, y):
        """
        A move is valid if the chosen cell is empty
        :param x: X coordinate
        :param y: Y coordinate
        :return: True if the board[x][y] is empty
        """
        self.x = x
        self.y = y
        if [self.get_x(), self.get_y()] in self.empty_cells():
            return True
        else:
            return False


    def set_move(self, x, y, player):
        """
        Set the move on board, if the coordinates are valid
        :param x: X coordinate
        :param y: Y coordinate
        :param player: the current player
        """
        self.player = player

        if self.valid_move(x, y):
            self.state[x][y] = self.player
            return True
        else:
            return False

class Play:
    """
    This class sets the human turn and ai turn by setting moves, validating moves and
    rendering the board.
    """

    # initialising the variables
    def __init__(self, c_choice, h_choice):
        self.c_choice = c_choice
        self.h_choice = h_choice

    def __str__(self):
        return ("The human choice for this game is "
        + self.h_choice.upper() + " and the computer choice is " + self.c_choice.upper()
        )

    def __repr__(self):
        return [self.c_choice.upper(), self.h_choice()]

    def ai_turn(self, c_choice, h_choice):
        """
        It calls the minimax function if the depth < 9,
        else it choices a random coordinate.
        :param c_choice: computer's choice X or O
        :param h_choice: human's choice X or O
        :return: None
        """
        if s.get_depth() == 0 or s.game_over():
            return

        clean()
        print(f'Computer turn [{self.c_choice}]')
        s.render(self.c_choice, self.h_choice)

        if s.get_depth() == 9:
            x = choice([0, 1, 2])
            y = choice([0, 1, 2])
        else:
            move = minimax(s.state, s.get_depth(), COMP)
            x, y = move[0], move[1]

        s.set_move(x, y, COMP)
        # Paul Lu.  Go full speed.
        # time.sleep(1)
    
    def human_turn(self, c_choice, h_choice):
        """
        The Human plays choosing a valid move.
        :param c_choice: computer's choice X or O
        :param h_choice: human's choice X or O
        :return: None
        """
    
        if s.get_depth() == 0 or s.game_over():
            return

        # Dictionary of valid moves
        move = -1
        moves = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
        }

        clean()
        print(f'Human turn [{self.h_choice}]')
        s.render(self.c_choice, self.h_choice)

        while move < 1 or move > 9:
            try:
                move = int(input('Use numpad (1..9): '))
                coord = moves[move]
                can_move = s.set_move(coord[0], coord[1], HUMAN)

                if not can_move:
                    print('Bad move')
                    move = -1
            except (EOFError, KeyboardInterrupt):
                print('Bye')
                exit()
            except (KeyError, ValueError):
                print('Bad choice')

def minimax(state, depth, player):
    """
    AI function that choice the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= 9),
    but never nine in this case (see iaturn() function)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    x = s.x
    y = s.y

    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if s.get_depth() == 0 or s.game_over():
        score = s.evaluate()
        return [-1, -1, score]

    for cell in s.empty_cells():
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(s.state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best

def clean():
    """
    Clears the console
    """
    # Paul Lu.  Do not clear screen to keep output human readable.
    print()
    return

    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')

def main():
    """
    Main function that calls all functions
    """
    # Paul Lu.  Set the seed to get deterministic behaviour for each run.
    #       Makes it easier for testing and tracing for understanding.
    randomseed(274 + 2020)

    # declaring the global variables
    global s
    global p
    global c_choice
    global h_choice
    global first

    clean()
    h_choice = ''  # X or O
    c_choice = ''  # X or O
    first = ''  # if human is the first

    # Human chooses X or O to play
    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Setting computer's choice
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    # Human may starts first
    clean()
    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    s = State(c_choice, h_choice)
    p = Play(c_choice, h_choice)

    # Main loop of this game
    while s.get_depth() > 0 and not s.game_over():
        if first == 'N':
            p.ai_turn(c_choice, h_choice)
            first = ''

        p.human_turn(c_choice, h_choice)
        p.ai_turn(c_choice, h_choice)

    # Game over message
    if s.wins(HUMAN):
        clean()
        print(f'Human turn [{h_choice}]')
        s.render(c_choice, h_choice)
        print('YOU WIN!')
    elif s.wins(COMP):
        clean()
        print(f'Computer turn [{c_choice}]')
        s.render(c_choice, h_choice)
        print('YOU LOSE!')
    else:
        clean()
        s.render(c_choice, h_choice)
        print('DRAW!')

    exit()

if __name__ == '__main__':
    main()
