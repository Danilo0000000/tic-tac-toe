print("Our board is like your numeric keypad, its a: \n 7,8.9\n 4,5,6\n 1,2,3")
class TicTacToe:
    board = {'7': ' ', '8': ' ', '9': ' ', '4': ' ', '5': ' ', '6': ' ', '1': ' ', '2': ' ', '3': ' '}
    turn = None
    def __init__(self, player_initial="X"):
        self.turn = player_initial

    def show_board(self):
        print("┌───┬───┬───┐")
        print(f"│ {self.board['7']} │ {self.board['8']} │ {self.board['9']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.board['4']} │ {self.board['5']} │ {self.board['6']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.board['1']} │ {self.board['2']} │ {self.board['3']} │")
        print("└───┴───┴───┘")

    def verify_move(self, move):
        if move in self.board.keys():
            if self.board[move] == " ":
                return True
        return False

    def verify_board(self):
        if self.board['7'] == self.board['4'] == self.board['1'] != ' ':
            return self.board['7']
        elif self.board['8'] == self.board['5'] == self.board['2'] != ' ':
            return self.board['8']
        elif self.board['9'] == self.board['6'] == self.board['3'] != ' ':
            return self.board['9']


        elif self.board['7'] == self.board['8'] == self.board['9'] != ' ':
            return self.board['7']
        elif self.board['4'] == self.board['5'] == self.board['6'] != ' ':
            return self.board['8']
        elif self.board['1'] == self.board['2'] == self.board['3'] != ' ':
            return self.board['1']

        elif self.board['7'] == self.board['5'] == self.board['3'] != ' ':
            return self.board['7']
        elif self.board['1'] == self.board['5'] == self.board['9'] != ' ':
            return self.board['1']


        if [*self.board.values()].count(' ') == 0:
            return "draw"
        else:
            return [*self.board.values()].count(' ')

    def play(self):

        while True:
            self.show_board()

            print(f"Turn of {self.turn}, what your play?")

            while True:
                move = input("play ")

                if self.verify_move(move): 
                    break  
                else:
                    print(f"play of {self.turn} invalid, play again.")

            self.board[move] = self.turn

            state = self.verify_board()

            if state == "X":
                print("X its a winner!!!")
                break

            elif state == "O":
                print("O its a winner!!!")
                break

            if state == "draw":
                print("draw!!!")
                break
            self.turn = "X" if self.turn == "O" else "O"

        self.show_board()


game = TicTacToe()

game.play()