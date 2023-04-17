import random

class Node:
    def __init__(self, board, player, moves):
        self.board = board
        self.player = player
        self.moves = moves


class TicTacToe2d:
    # " char list containing X and O "
    board = []

    magicSquare = [
        4, 9, 2,
        3, 5, 7,
        8, 1, 6,
    ]
    usedSquarePosition = []
    round = 0
    positionsByCpu = []
    positionsByHuman = []

    def __init__(self):
        self.board = [
            '_' for i in range(9)
        ]

        for i in range(1000):
            self.round = i
            # print(i)
            if i % 2 == 0:
                self.take_user_input()
                if self.hasWon('X'):
                    print("-----Congratulations!!-----")
                    print("Player Wins!!")
                    break
                elif self.isGameOver():
                    break

            else:
                self.computer_input()
                if self.hasWon('O'):
                    print("-----Better Luck Next Time-----")
                    print("Computer Wins!!")
                    break
                elif self.isGameOver():
                    break

    #     user prompt for position( 0.. 9)

    def take_user_input(self):
        print("It is your turn: ")
        ip = (input("Choose a position (0-8):"))
        # for simplicity assume user is x and runs first
        # self.board[ip] = 'X'
        while (ip.isdigit()==False) or (int(ip) in self.usedSquarePosition) or (int(ip)>8):
            print("Invalid input")
            ip = (input("Choose a position (0-8):"))
        
        ip = int(ip)
        self.board[ip] = 'X'
        self.usedSquarePosition.append(ip)
        self.positionsByHuman.append(ip)
        self.display_board()

    def display_board(self):
        print("=========")
        for i in range(9):
            if i % 3 == 0:
                print()
                print("|", end=' ')
                print(self.board[i], end=' ')
            else:
                print(self.board[i], end=' ')
                if i % 3 == 2:
                    print("|")
                
        # print("\n")
        print("=========")

    def computer_input(self):
        print("Computer's turn !!")
        node = Node(self.board, 'O', self.get_available_moves())
        move = self.minimax(node)
        self.board[move] = 'O'
        self.usedSquarePosition.append(move)
        self.positionsByCpu.append(move)
        self.display_board()

    def minimax(self, node):
        if self.hasWon('X'):
            return -1

        if self.hasWon('O'):
            return 1

        if len(node.moves) == 0:
            return 0

        scores = []
        for move in node.moves:
            new_board = node.board.copy()
            new_board[move] = node.player
            new_player = 'X' if node.player == 'O' else 'O'
            new_moves = self.get_available_moves(new_board)

            new_node = Node(new_board, new_player, new_moves)
            score = self.minimax(new_node)
            scores.append(score)

        if node.player == 'O':
            max_score = max(scores)
            return node.moves[scores.index(max_score)]
        else:
            min_score = min(scores)
            return node.moves[scores.index(min_score)]
        
    def get_available_moves(self, board=None):
        if board is None:
            board = self.board

        return [i for i, x in enumerate(board) if x == '_']


    def get_blocking_move(self):
        for j in self.positionsByHuman:
            for k in self.positionsByHuman:
                if j != k:
                    for i in range(9):
                        if i not in self.usedSquarePosition:
                            if self.magicSquare[i] + self.magicSquare[j] + self.magicSquare[k] == 15:
                                return i
        return -404

    def isGameOver(self):
        if '_' not in self.board:
            return True
        else:
            return False

    def hasWon(self, player):
        for i in range(9):
            for j in range(9):
                for k in range(9):
                    if (i != j and i != k and j != k):
                        if self.board[i] == player and self.board[j] == player and self.board[k] == player:
                            if self.magicSquare[i] + self.magicSquare[j] + self.magicSquare[k] == 15:
                                return True
        return False

    def think(self):
        for j in range(9):
            if self.magicSquare[j] > 6 and j not in self.usedSquarePosition:
                return j

    def get_winning_move(self):
        # print("here")
        for j in self.positionsByCpu:
            for k in self.positionsByCpu:
                if j != k:
                    for i in range(9):
                        if i not in self.usedSquarePosition:
                            if (self.magicSquare[i] + self.magicSquare[j] + self.magicSquare[k] == 15):
                                return i
        return -404


if __name__ == "__main__":
    TicTacToe2d()
