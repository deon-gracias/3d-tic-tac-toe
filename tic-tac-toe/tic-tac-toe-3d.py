from ursina import *
import numpy as np
from ursina.prefabs.first_person_controller import FirstPersonController

board_entities = []

board = np.zeros((3, 3, 3))  # initialize 3D array to represent game board

board3d = []
magicSquare = [
    4, 9, 2,
    3, 5, 7,
    8, 1, 6,
    4, 9, 2,
    3, 5, 7,
    8, 1, 6,
    4, 9, 2,
    3, 5, 7,
    8, 1, 6,
]
brd = ["_" for i in range(27)]
usedSquarePosition = []
positionsByCpu = []
positionsByHuman = []
game_over = False

turn = 0

colors = {
    'white': color.rgba(255, 255, 255, 255),
    'red': color.rgba(255, 0, 0, 255),
    'blue': color.rgba(0, 0, 255, 255),
}

app = Ursina()


class Cube(Entity):

    def __init__(self, origin_x=0, origin_y=0, origin_z=0, i_index=0, j_index=0, k_index=0, magic_num=0, index=0):
        super().__init__(
            model='cube',
            texture='white_cube',
            color=colors['white'],
            collider='box',
            origin_x=origin_x,
            origin_y=origin_y,
            origin_z=origin_z,
        )

        self.marked = 'none'
        self.i_index = i_index
        self.j_index = j_index
        self.k_index = k_index
        self.magic_num = magic_num
        self.index = index

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                mark_cube(self)
                if not game_over:
                    ai_move()


def ai_move():
    global turn
    global board3d

    available_cubes = [c for c in board3d if c.marked == 'none']
    if not available_cubes:
        return  # no available moves
    # cube = random.choice(available_cubes)
    nice_index = get_winning_move()
    for c in available_cubes:
        if c.index == nice_index:
            cube = c
            break
    else:
        cube = random.choice(available_cubes)
    mark_cube(cube)


def isGameOver():
    global game_over
    global board
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if board[i][j][k] == 0:
                    # print("here")
                    return
    game_over = True
    print("Game Over \n")
    pass


def mark_cube(e):
    isGameOver()
    hasWon('X')
    hasWon('O')

    if e.marked != 'none':
        return

    global turn
    global board
    usedSquarePosition.append(e.index)
    turn += 1

    if turn % 2 == 0:
        e.marked = 'red'
        e.color = colors['red']
        positionsByHuman.append(e.index)
        board[e.i_index, e.j_index, e.k_index] = 1
        brd[e.index] = 'X'

    else:
        e.marked = 'blue'
        e.color = colors['blue']
        positionsByCpu.append(e.index)
        board[e.i_index, e.j_index, e.k_index] = 2
        brd[e.index] = 'O'
    print(positionsByCpu)
    print(positionsByHuman)
    print(len(usedSquarePosition))


def hasWon(player):
    global brd
    global magicSquare
    for i in range(27):
        for j in range(27):
            for k in range(27):
                if i != j and i != k and j != k:
                    if brd[i] == player and brd[j] == player and brd[k] == player:
                        if magicSquare[i] + magicSquare[j] + magicSquare[k] == 15:
                            print(f"player {player} won the game!!\n")
                            return True
                        elif magicSquare[i] == magicSquare[j] == magicSquare[k]:
                            print(f"player {player} won the game!!\n")
                            return True
    return False


def think():
    global magicSquare
    for j in range(9):
        if magicSquare[j] > 6 and j not in usedSquarePosition:
            return j


def get_winning_move():
    # print("here")
    for j in positionsByCpu:
        for k in positionsByCpu:
            if j != k:
                for i in range(27):
                    if i not in usedSquarePosition:
                        if magicSquare[i] + magicSquare[j] + magicSquare[k] == 15:
                            return i

def get_blocking_move(self):
        for j in positionsByHuman:
            for k in positionsByHuman:
                if j != k:
                    for i in range(9):
                        if i not in usedSquarePosition:
                            if magicSquare[i] + magicSquare[j] + magicSquare[k] == 15:
                                return i
                            elif magicSquare[i] == magicSquare[j] == magicSquare[k]:
                                return i

        return -404

def check_and_draw_lines_2d(cor_1, cor_2, cor_3):
    x1 = cor_1.x
    x2 = cor_2.x
    x3 = cor_3.x
    y1 = cor_1.y
    y2 = cor_2.y
    y3 = cor_3.y
    z1 = cor_1.z
    z2 = cor_2.z
    z3 = cor_3.z


#


def check_2d_lines(cor_1, cor_2, cor_3):
    pass


def create_assets():
    index = 0
    x = 0
    y = 0
    z = 0
    global magicSquare
    for i in np.linspace(-2, 2, 3):
        # board3d = []
        global  board3d
        for j in np.linspace(-2, 2, 3):
            for k in np.linspace(-1, 2, 3):
                e = Cube(
                    origin_y=i,
                    origin_x=j,
                    origin_z=k,
                    magic_num=magicSquare[index],
                    index=index,
                    i_index=x,
                    j_index=y,
                    k_index=z
                )
                board3d.append(e)
                index += 1
                z = (z + 1) % 3
            y = (y + 1) % 3
        x = (x + 1) % 3
        board_entities.append(board)


EditorCamera()


def main():
    create_assets()
    player = FirstPersonController()
    app.run()


if __name__ == "__main__":
    main()
