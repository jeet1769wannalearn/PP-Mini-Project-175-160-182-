from random import randint


def TicTacToe():
    def printBoard(board):
        for i in range(3):
            print(board[i * 3] + "|" + board[i * 3 + 1] + "|" + board[i * 3 + 2])
            if i is not 2:
                print("-----")

    board = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " ",]

    winning = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    win = False
    token = "X"
    winner = ""
    draw = True
    printBoard(board)
    while not win:
        error = True
        while error:
            index = int(input("Enter " + token + "'s move (0-8): "))
            if index <= 8 and index >= 0 and board[index] == " ":
                board[index] = token
                error = False
        printBoard(board)
        token = "O" if token == "X" else "X"
        draw = True
        for states in winning:
            str = ""
            for indice in states:
                if board[indice] == " ":
                    draw = False
                str = str + board[indice]
            if str == "XXX" or str == "OOO":
                win = True
                winner = str[0]
    if not draw:
        print("Winner is : " + winner)
    else:
        print("Draw!")


def Battleship():
    def checkShipPlacement(board, shiplen, x, y, horizontal):
        if horizontal:
            if 0 <= x <= 10 - shiplen and 0 <= y < 10:
                for i in range(shiplen):
                    if board[y][x + i] is not " ":
                        return False
            else:
                return False
        else:
            if 0 <= y <= 10 - shiplen and 0 <= x < 10:
                for i in range(shiplen):
                    if board[y + i][x] is not " ":
                        return False
            else:
                return False
        return True

    def placeShip(board, shiplen, x, y, horizontal):
        if horizontal:
            for i in range(shiplen):
                board[y][x + i] = str(shiplen)
        else:
            for i in range(shiplen):
                board[y + i][x] = str(shiplen)

    def computerPlace(board):
        for i in range(5):
            successful = False
            x = 0
            y = 0
            horiz = False
            while not successful:
                x = randint(0, 9)
                y = randint(0, 9)
                horiz = randint(0, 1) == 1
                successful = checkShipPlacement(board, i + 1, x, y, horiz)
            placeShip(board, i + 1, x, y, horiz)

    def playerPlace(board):
        for i in range(5):
            successful = False
            x = 0
            y = 0
            horiz = False
            while not successful:
                loc = input("Enter location of ship size " + str(i + 1) + " in (A0) format (A-J),(0-9): ").upper()
                x = ord(loc[0]) - 65
                y = int(loc[1])
                horiz = input("Enter 0 for vertical and 1 for horizontal: ")
                horiz = False if horiz[0] == "0" else True
                successful = checkShipPlacement(board, i + 1, x, y, horiz)
            placeShip(board, i + 1, x, y, horiz)

    def checkWin(board):
        for row in board:
            for element in row:
                if element is not "X" or element is not " " or element is not "O":
                    return False
        return True

    def printBoard(board, censor):
        print("   A B C D E F G H I J")
        for row in range(len(board)):
            print(str(row)+"| ", end="")
            for element in board[row]:
                a = element
                if censor:
                    if element is not "X" and  element is not "O" and element is not " ":
                        a = " "
                print(a + " ", end="")
            print()


    def makeMove(board, x, y, turn):
        if 0 <= x < 10 and 0 <= y < 10:
            if board[y][x] is not "X" and board[y][x] is not "O":
                token = "X"
                if board[y][x] is not " ":
                    print(turn+" had a succesful hit!")
                    token = "O"
                board[y][x] = token
                return True
            else:
                return False
        else:
            return False

    win = False
    computerBoard = []
    playerBoard = []
    for i in range(10):
        computerBoard.append([" ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
        playerBoard.append([" ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
    computerPlace(computerBoard)
    playerPlace(playerBoard)
    turn = "Player"
    while not win:
        print("Computer's Board")
        printBoard(computerBoard, True)
        print()
        print("Player's Board")
        printBoard(playerBoard, False)

        if turn == "Player":
            print("-------------------------\n\n")
            succesful = False
            x = 0
            y = 0
            while not succesful:
                loc = input("Enter location of attack in (A0) format (A-J),(0-9): ").upper()
                x = ord(loc[0]) - 65
                y = int(loc[1])
                succesful = makeMove(computerBoard, x, y, turn)
            turn = "Computer"
        else:
            print("----------------------------------------------------\n\n")
            succesful = False
            x = 0
            y = 0
            while not succesful:
                x = randint(0, 9)
                y = randint(0, 9)
                succesful = makeMove(playerBoard, x, y, turn)
            turn = "Player"

        win = checkWin(playerBoard) or checkWin(computerBoard)

    if checkWin(playerBoard):
        print("Computer Wins")
    else:
        print("Player Wins")


def menu():
    exit = False
    while not exit:
        print("Enter 1 for TicTacToe")
        print("Enter 2 for Battleship")
        print("Enter 3 to Exit")
        selection = input("Enter your option: ")
        if selection == "1":
            TicTacToe()
        elif selection == "2":
            Battleship()
        elif selection == "3":
            print("Exiting!")
            exit = True
        else:
            "Unknown option!"


menu()
