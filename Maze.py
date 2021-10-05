# coding=utf-8
import random
import inspect

from Room import *


class Maze:

    # Here’s the mile-high view of recursive backtracking: Choose a starting point in the field. Randomly choose a
    # wall at that point and carve a passage through to the adjacent cell, but only if the adjacent cell has not been
    # visited yet. This becomes the new current cell. If all adjacent cells have been visited, back up to the last
    # cell that has un-carved walls and repeat. The algorithm ends when the process has backed all the way up to the
    # starting point.

    def __init__(self):
        self.size = int(input('Input a integer: '))
        self.maze = [[Room() for i in range(0, self.size)] for j in range(0, self.size)]

    def getRandCoord(self):
        return random.randrange(0, len(self.maze))

    def getRandCard(self, room):
        if room.getName() == "room":
            card = ["N", "S", "E", "W"]
            method = [room.getN(), room.getS(), room.getE(), room.getW()]
            rand = random.randrange(0, 4)
            return method[rand], card[rand]
        else:
            return False

    def checkAxis(self, room, start):
        check = maze.getRandCard(maze.maze[start[0]][start[1]])


    def printBoard(self, depth=None):
        if depth:
            for row in maze.maze:
                for col in row:
                    print(col)
        else:
            for row in maze.maze:
                print(row)
        return


maze = Maze()
start = [maze.getRandCoord(), maze.getRandCoord()]  # start[X,Y]

print(maze.getRandCard(maze.maze[start[0]][start[1]]))
