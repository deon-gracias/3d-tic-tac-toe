from ursina import *
from PIL import Image
import numpy as np

board_entities = []

turn = 0

colors = {
    'white': color.rgba(255, 255, 255, 20),
    'red': color.rgba(255, 0, 0, 120),
    'blue': color.rgba(0, 0, 255, 120),
}

app = Ursina()


class Square(Entity):

    def __init__(self, origin_x=0, origin_y=0, origin_z=0):
        super().__init__(
            model='plane',
            color=colors['white'],
            collider='box',
            origin_x=origin_x,
            origin_y=origin_y,
            origin_z=origin_z,
        )

        self.marked = 'none'

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                mark_square(self)
                # destroy(self)


def mark_square(e):
    if e.marked != 'none':
        return

    global turn
    turn += 1

    if turn % 2 == 0:
        e.marked = 'red'
        e.color = colors['red']
    else:
        e.marked = 'blue'
        e.color = colors['blue']


def create_assets():
    for i in np.linspace(-1, 2, 3):
        board = []
        for j in np.linspace(-1, 2, 3):
            for k in np.linspace(-1, 2, 3):
                e = Square(
                    origin_y=i,
                    origin_x=j,
                    origin_z=k,
                )
                board.append(e)
        board_entities.append(board)


EditorCamera()


def main():
    create_assets()
    app.run()


if __name__ == "__main__":
    main()
