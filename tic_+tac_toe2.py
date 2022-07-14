
board =["-","-","-",
        "-","-","-",
        "-","-","-",]
current_player = "X"
winner = None
gamerunning = True
multiplayer_variable = "O"
for_multiploayer_variable2 = "X"
def printing_Board(board):
        print("WELCOM TO TIC TAC TOE")
        print(board[0] + "|" + board[1] + "|" + board[2])
        print("-----")
        print(board[3] + "|" + board[4] + "|" + board[5])
        print("-----")
        print(board[6] + "|" + board[7] + "|" + board[8])


def plyerInput(board):
        while True:
                command = int(input("Enter a number between 1-9 according to the dashes:"))
                if command >= 1 and command <= 9 and board[command-1] == "-":
                        board[command-1] = current_player
                        break
                else:
                        print("Error the box is already filled")

def check_rows(board):
        global winner
        if board[0] == board[1] == board[2] and board[0] != "-":
                winner = board[0]
                return True

        elif board[3] == board[4] == board[5] and board[3] != "-":
                winner = board[3]
                return True
        elif board[6] == board[7] == board[8] and board[6] != "-":
                winner = board[6]
                return True

def check_colubs():
        global winner
        if board[0] == board[3] == board[6] and board[0] != "-":
                winner = board[0]
                return True
        elif board[1] == board[4] == board[7] and board[1] != "-":
                winner = board[1]
                return True
        elif board[2] == board[5] == board[8] and board[2] != "-":
                winner = board[2]
                return True

def check_diagnal(board):
        global winner
        if board[0] == board[4] == board[8] and board[0] != "-":
                winner = board[0]
                return True
        elif board[2] == board[4] == board[6] and board[2] != "-":
                winner = board[2]
                return True
def check_Tie(board):
        global gamerunning
        if "-" not in board:
                printing_Board(board)
                print("It is a tie")
                gamerunning = True
                reset_board()
                printing_Board(board)


def check_win():
        if check_diagnal(board) or check_colubs() or check_rows(board):
                print(f"The winner is {winner}")
                print("THANK YOU FOR PLAYING")
                reset_board()
                printing_Board(board)
def reset_board():
        global board
        board = ["-","-","-",
                 "-","-","-",
                 "-","-","-",]

def switch_player():
        global current_player
        if current_player == "X":
                current_player = "O"
        else:
                current_player = "X"


def computer_multiplayer(board):
        while current_player == "O":
            if board[4] == "-":
                board[4] = "O"
                switch_player()
            #todo new code
            elif board[0] and board[1] == for_multiploayer_variable2 and board[2] == "-":
                board[2] = "O"
                switch_player()

            elif board[1] and board[2] == for_multiploayer_variable2 and board[0] == "-":
                board[0] = "O"
                switch_player()

            elif board[0] and board[2] == for_multiploayer_variable2 and board[1] == "-":
                board[1] = "O"
                switch_player()

            elif board[3] and board[4] == for_multiploayer_variable2 and board[5] == "-":
                board[5] = "O"
                switch_player()

            elif board[4] and board[5] == for_multiploayer_variable2 and board[3] == "-":
                board[3] = "O"
                switch_player()

            elif board[3] and board[5] == for_multiploayer_variable2 and board[4] == "-":
                board[4] = "O"
                switch_player()

            elif board[6] and board[7] == for_multiploayer_variable2 and board[8] == "-":
                board[8] = "O"
                switch_player()

            elif board[7] and board[8] == for_multiploayer_variable2 and board[6] == "-":
                board[6] = "O"
                switch_player()

            elif board[6] and board[8] == for_multiploayer_variable2 and board[7] == "-":
                board[7] = "O"
                switch_player()

            #todo columds
            elif board[0] and board[3] == for_multiploayer_variable2 and board[6] == "-":
                board[6] = "O"
                switch_player()

            elif board[3] and board[6] == for_multiploayer_variable2 and board[0] == "-":
                board[0] = "O"
                switch_player()

            elif board[0] and board[6] == for_multiploayer_variable2 and board[3] == "-":
                board[3] = "O"

            elif board[1] and board[4] == for_multiploayer_variable2 and board[7] == "-":
                board[7] = "O"
                switch_player()

            elif board[4] and board[7] == for_multiploayer_variable2 and board[1] == "-":
                board[1] = "O"
                switch_player()

            elif board[1] and board[7] == for_multiploayer_variable2 and board[4] == "-":
                board[4] = "O"
                switch_player()

            elif board[2] and board[5] == for_multiploayer_variable2 and board[8] == "-":
                board[8] = "O"
                switch_player()

            elif board[5] and board[8] == for_multiploayer_variable2 and board[2] == "-":
                board[2] = "O"
                switch_player()

            elif board[2] and board[8] == for_multiploayer_variable2 and board[5] == "-":
                board[5] = "O"
                switch_player()

            #todo diagnol
            elif board[0] and board[4] == for_multiploayer_variable2 and board[8] == "-":
                board[8] = "O"
                switch_player()

            elif board[4] and board[8] == for_multiploayer_variable2 and board[6] == "-":
                board[6] = "O"
                switch_player()

            elif board[0] and board[8] == for_multiploayer_variable2 and board[4] == "-":
                board[4] = "O"
                switch_player()

            elif board[2] and board[4] == for_multiploayer_variable2 and board[6] == "-":
                board[6] = "O"
                switch_player()

            elif board[6] and board[4] == for_multiploayer_variable2 and board[2] == "-":
                board[2] = "O"
                switch_player()

            elif board[6] and board[2] == for_multiploayer_variable2 and board[4] == "-":
                board[4] = "O"
                switch_player()

                # todo win
            elif board[0] and board[1] == multiplayer_variable and board[2] == "-":
                board[2] = "O"
                switch_player()
            elif board[1] and board[2] == multiplayer_variable and board[0] == "-":
                board[0] = "O"
                switch_player()
            elif board[0] and board[2] == multiplayer_variable and board[1] == "-":
                board[1] = "O"
                switch_player()
            elif board[0] and board[1] == multiplayer_variable and board[2] == "-":
                board[2] = "O"
                switch_player()
            elif board[3] and board[4] == multiplayer_variable and board[5] == "-":
                board[5] = "O"
                switch_player()
            elif board[3] and board[5] == multiplayer_variable and board[4] == "-":
                board[4] = "O"
                switch_player()
            elif board[4] and board[5] == multiplayer_variable and board[3] == "-":
                board[3] = "O"
                switch_player()
            elif board[6] and board[7] == multiplayer_variable and board[8] == "-":
                board[8] = "O"
                switch_player()
            elif board[6] and board[8] == multiplayer_variable and board[7] == "-":
                board[7] = "O"
                switch_player()
            elif board[7] and board[8] == multiplayer_variable and board[6] == "-":
                board[6] = "O"
                switch_player()
            elif board[0] and board[3] == multiplayer_variable and board[6] == "-":
                board[6] = "O"
                switch_player()
            elif board[0] and board[6] == multiplayer_variable and board[3] == "-":
                board[3] = "O"
                switch_player()
            elif board[3] and board[6] == multiplayer_variable and board[0] == "-":
                board[0] = "O"
                switch_player()
            elif board[1] and board[4] == multiplayer_variable and board[7] == "-":
                board[7] = "O"
                switch_player()
            elif board[1] and board[7] == multiplayer_variable and board[4] == "-":
                board[4] = "O"
                switch_player()
            elif board[4] and board[7] == multiplayer_variable and board[1] == "-":
                board[1] = "O"
                switch_player()
            elif board[2] and board[5] == multiplayer_variable and board[8] == "-":
                board[8] = "O"
                switch_player()
            elif board[2] and board[8] == multiplayer_variable and board[5] == "-":
                board[5] = "O"
                switch_player()
            elif board[5] and board[8] == multiplayer_variable and board[2] == "-":
                board[2] = "O"
                switch_player()
            elif board[2] and board[4] == multiplayer_variable and board[6] == "-":
                board[6] = "O"
                switch_player()
            elif board[6] and board[4] == multiplayer_variable and board[2] == "-":
                board[2] = "O"
                switch_player()
            elif board[6] and board[2] == multiplayer_variable and board[4] == "-":
                board[4] = "O"
                switch_player()
            elif board[0] and board[4] == multiplayer_variable and board[8] == "-":
                board[8] = "O"
                switch_player()
            elif board[4] and board[8] == multiplayer_variable and board[0] == "-":
                board[0] = "O"
                switch_player()
            elif board[0] and board[8] == multiplayer_variable and board[4] == "-":
                board[4] = "O"
                switch_player()
          #todo rows
            elif for_multiploayer_variable2 == board[0] and board[1] == "-":
                board[1] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[0] and board[3] == "-":
                board[3] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[2] and board[1] == "-":
                board[1] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[2] and board[5] == "-":
                board[5] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[1] and board[0] == "-":
                board[0] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[1] and board[4] == "-":
                board[4] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[1] and board[2] == "-":
                board[2] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[3] and board[4] == "-":
                board[4] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[3] and board[6] == "-":
                board[6] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[3] and board[0] == "-":
                board[0] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[4] and board[3] == "-":
                board[3] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[4] and board[5] == "-":
                board[5] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[4] and board[1] == "-":
                board[1] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[4] and board[7] == "-":
                board[7] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[5] and board[4] == "-":
                board[4] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[5] and board[2] == "-":
                board[2] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[5] and board[8] == "-":
                board[8] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[6] and board[7] == "-":
                board[7] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[6] and board[3] == "-":
                board[3] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[7] and board[6] == "-":
                board[6] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[7] and board[8] == "-":
                board[8] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[7] and board[4] == "-":
                board[4] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[8] and board[7] == "-":
                board[7] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[8] and board[5] == "-":
                board[5] = "O"
                switch_player()

            #todo columbs
            elif for_multiploayer_variable2 == board[0] and board[3] == "-":
                board[3] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[0] and board[1] == "-":
                board[1] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[3] and board[0] == "-":
                board[0] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[3] and board[6] == "-":
                board[6] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[3] and board[4] == "-":
                board[4] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[1] and board[4] == "-":
                board[4] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[1] and board[0] == "-":
                board[0] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[1] and board[2] == "-":
                board[2] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[4] and board[7] == "-":
                board[7] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[4] and board[1] == "-":
                board[1] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[4] and board[3] == "-":
                board[3] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[4] and board[5] == "-":
                board[5] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[7] and board[4] == "-":
                board[4] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[7] and board[6] == "-":
                board[6] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[7] and board[8] == "-":
                board[8] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[2] and board[5] == "-":
                board[5] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[2] and board[1] == "-":
                board[1] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[5] and board[2] == "-":
                board[2] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[5] and board[8] == "-":
                board[8] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[5] and board[4] == "-":
                board[4] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[8] and board[5] == "-":
                board[5] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[8] and board[7] == "-":
                board[7] = "O"
                switch_player()

            #todo diagnol
            elif for_multiploayer_variable2 == board[2] and board[4] == "-":
                board[4] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[2] and board[1] == "-":
                board[1] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[2] and board[5] == "-":
                board[5] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[4] and board[2] == "-":
                board[2] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[4] and board[6] == "-":
                board[6] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[4] and board[1] == "-":
                board[1] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[4] and board[7] == "-":
                board[7] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[4] and board[5] == "-":
                board[5] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[4] and board[3] == "-":
                board[3] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[4] and board[0] == "-":
                board[0] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[4] and board[2] == "-":
                board[2] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[4] and board[6] == "-":
                board[6] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[4] and board[8] == "-":
                board[8] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[6] and board[4] == "-":
                board[4] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[6] and board[3] == "-":
                board[3] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[6] and board[7] == "-":
                board[7] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[0] and board[4] == "-":
                board[4] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[0] and board[1] == "-":
                board[1] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[4] and board[3] == "-":
                board[3] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[4] and board[0] == "-":
                board[0] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[4] and board[8] == "-":
                board[8] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[8] and board[4] == "-":
                board[4] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[8] and board[5] == "-":
                board[5] = "O"
                switch_player()

            elif for_multiploayer_variable2 == board[8] and board[7] == "-":
                board[7] = "O"
                switch_player()
while gamerunning:
        printing_Board(board)
        plyerInput(board)
        check_rows(board)
        check_colubs()
        check_diagnal(board)
        check_Tie(board)
        check_win()
        switch_player()
        computer_multiplayer(board)
        check_rows(board)
        check_colubs()
        check_diagnal(board)
        check_Tie(board)

