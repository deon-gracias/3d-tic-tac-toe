import pygame
from pygame.locals import *
from turtle import Turtle, Screen
import numpy as np

from missionaries_and_cannibals import MissionariesAndCannibals
from search import iterative_deepening_search


boat = [None, None]
boat_seats = [[-250, 0], [-200, 0]]
left = {"missionaries": [], "cannibals": []}
right = {"missionaries": [], "cannibals": []}


def put_in_boat(turtle):
    if None not in boat:
        return False

    empty_index = boat.index(None)
    turtle.goto(boat_seats[empty_index][0], boat_seats[empty_index][1])
    boat[empty_index] = turtle


def move_boat(forward):
    for turtle in boat:
        if turtle is not None:
            turtle.forward(forward)


def animate(path):
    temp = path[0].state.value
    for node in path[1:]:
        # Boat on the other side
        if node.state.value[2] == 0:
            move_boat(300)

def main(result):
    # Initialise screen
    screen = Screen()
    screen.setup(width=800, height=600)

    colors = ['red', 'blue']

    # y_positions = [-260, -172, -85, 2, 85, 172, 260]
    n = 6
    (start, end) = (-260, 260)
    step = (end - start) / float(n - 1)
    y_positions = [int(round(start + x * step))
                   for x in range(n)]  # Generate evenly spaced coordinates

    turtles = []  # Storing turtles

    for index in range(len(y_positions)):
        new_tur = Turtle(shape="turtle")
        new_tur.shapesize(2)

        new_tur.speed('fastest')
        new_tur.penup()

        new_tur.goto(x=-350, y=y_positions[index])

        new_tur.speed('slowest')
        turtles.append(new_tur)

    # Assign colors
    for turtle in turtles[:3]:
        turtle.color(colors[0])  # Cannibals
        left["cannibals"].append(turtle)

    for turtle in turtles[3:]:
        turtle.color(colors[1])  # Missionaries
        left["missionaries"].append(turtle)

    # Put in boat
    # for turtle in turtles: put_in_boat(turtle)

    # Simulate
    animate(result)

    screen.exitonclick()


def solve():
    problem = MissionariesAndCannibals()
    result = iterative_deepening_search(problem)
    return result.path()


if __name__ == '__main__':
    result = solve()
    main(result)
