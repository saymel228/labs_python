import PySimpleGUI as sg
from enum import Enum

class Player(Enum):
    X = 'X'
    O = 'O'
    EMPTY = ' '

class TicTacToeException(Exception):
    pass

class InvalidMoveException(TicTacToeException):
    pass

class GameOverException(TicTacToeException):
    pass

class TicTacToe:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.board = [[Player.EMPTY for _ in range(3)] for _ in range(3)]
        self.current_player = Player.X
        self.game_over = False
        self.winner = None
    
    def make_move(self, row, col):
        if self.game_over:
            raise GameOverException("Игра уже завершена")
        
        if not (0 <= row < 3 and 0 <= col < 3):
            raise InvalidMoveException("Некорректные координаты")
        
        if self.board[row][col] != Player.EMPTY:
            raise InvalidMoveException("Клетка уже занята")
        
        self.board[row][col] = self.current_player
        
        if self.check_winner():
            self.winner = self.current_player
            self.game_over = True
        elif self.is_board_full():
            self.game_over = True
        else:
            self.switch_player()
    
    def switch_player(self):
        self.current_player = Player.O if self.current_player == Player.X else Player.X
    
    def check_winner(self):
        for i in range(3):
            if (self.board[i][0] == self.board[i][1] == self.board[i][2] != Player.EMPTY or
                self.board[0][i] == self.board[1][i] == self.board[2][i] != Player.EMPTY):
                return True
        
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] != Player.EMPTY or
            self.board[0][2] == self.board[1][1] == self.board[2][0] != Player.EMPTY):
            return True
        
        return False
    
    def is_board_full(self):
        return all(cell != Player.EMPTY for row in self.board for cell in row)
    
    def get_board_state(self):
        return [[cell.value for cell in row] for row in self.board]

class TicTacToeGUI:
    def __init__(self):
        self.game = TicTacToe()
        
        try:
            sg.theme('LightBlue2')  
        except AttributeError:
            sg.ChangeLookAndFeel('LightBlue2')  
            
        self.window = self.create_window()
    
    def create_window(self):
        board = [
            [sg.Button('', size=(4, 2), key=f'{i},{j}', pad=(0,0))
            for j in range(3)]
            for i in range(3)
        ]
        
        layout = [
            [sg.Text('Ход: X', key='-TURN-', font=('Helvetica', 14))],
            *board,
            [sg.Button('Новая игра'), sg.Button('Выход')]
        ]
        
        return sg.Window('Крестики-нолики', layout)
    
    def update_ui(self):
        board_state = self.game.get_board_state()
        for i in range(3):
            for j in range(3):
                self.window[f'{i},{j}'].update(board_state[i][j])

        if self.game.game_over:
            status = 'Ничья!' if not self.game.winner else f'Победил {self.game.winner.value}!'
        else:
            status = f'Ход: {self.game.current_player.value}'
        
        self.window['-TURN-'].update(status)
    
    def run(self):
        while True:
            event, values = self.window.read()
            
            if event in (sg.WIN_CLOSED, 'Выход'):
                break
            
            if event == 'Новая игра':
                self.game.reset()
                self.update_ui()
                continue

            if ',' in event and not self.game.game_over:
                try:
                    row, col = map(int, event.split(','))
                    self.game.make_move(row, col)
                    self.update_ui()
                except TicTacToeException as e:
                    sg.popup_error(str(e))
        
        self.window.close()

if __name__ == '__main__':
    gui = TicTacToeGUI()
    gui.run()