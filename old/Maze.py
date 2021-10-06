# coding=utf-8
import random
from Room import *


class Maze:
    # Here’s the mile-high view of recursive backtracking:
    # Choose a starting point in the field.
    # Randomly choose a wall at that point and carve a passage through to the adjacent cell,
    # but only if the adjacent cell has not been visited yet.
    # This becomes the new current cell.
    # If all adjacent cells have been visited, back up to the last cell that has un-carved walls and repeat.
    # The algorithm ends when the process has backed all the way up to the starting point.

    def __init__(self, dimension):
        self.size = dimension
        self.maze = [[Room() for i in range(0, self.size)] for j in range(0, self.size)]
        self.card = ["N", "S", "E", "W"]
        # currPos = [X,Y]
        self.currPos = None
        self.end = [self.size - 1, self.size - 1]

    def getCurrPos(self):
        return self.currPos

    def setCurrPos(self, pos):
        self.currPos = pos
        return self

    def getRandCoord(self):
        return random.randrange(0, self.size) - 1

    def getRandCard(self):
        return self.card[random.randrange(0, 3)]

    def check(self, pos, card):
        # take the current position and check the room at the desired card
        # pos = [X,Y]
        if card == "N" and self.maze[pos[0]][pos[1] - 1]:
            return self.maze[pos[0]][pos[1] - 1].getIsVisited()
        elif card == "S" and self.maze[pos[0]][pos[1] + 1]:
            return self.maze[pos[0]][pos[1] + 1].getIsVisited()
        elif card == "E" and self.maze[pos[0] + 1][pos[1]]:
            return self.maze[pos[0] + 1][pos[1]].getIsVisited()
        elif card == "W" and self.maze[pos[0] - 1][pos[1]]:
            return self.maze[pos[0] - 1][pos[1]].getIsVisited()

    def carve(self, pos):
        # take the current position and check the room at the desired card
        # pos = [X,Y]
        self.setCurrPos([pos[0], pos[1]])
        while self.maze[self.end[0]][self.end[1]].getIsVisited() == False:
            card = self.getRandCard()
            if card == "N":
                if 0 <= pos[1] - 1 < self.size:
                    try:
                        north = self.maze[pos[0]][pos[1] - 1]
                        if not north.getIsVisited():
                            self.maze[pos[0]][pos[1]].setIsVisited(True)
                            self.maze[pos[0]][pos[1]].setN(True)
                            self.setCurrPos([pos[0], pos[1] - 1])

                            return self.carve([self.getCurrPos()[0], self.getCurrPos()[1]])
                    except IndexError:
                        continue
                    # finally:
                    #     print(["N", pos[0], pos[1] - 1])
                return self.carve([self.getRandCoord(), self.getRandCoord()])

            if card == "S":
                if 0 <= pos[1] + 1 < self.size:
                    try:
                        south = self.maze[pos[0]][pos[1] + 1]
                        if not south.getIsVisited():
                            self.maze[pos[0]][pos[1]].setS(True)
                            self.maze[pos[0]][pos[1]].setIsVisited(True)
                            self.setCurrPos([pos[0], pos[1] + 1])
                            return self.carve([self.getCurrPos()[0], self.getCurrPos()[1]])
                    except IndexError:
                        continue
                    # finally:
                    #     print(["S", pos[0], pos[1] + 1])

                return self.carve([self.getRandCoord(), self.getRandCoord()])

            if card == "E":
                if 0 <= pos[0] + 1 < self.size:
                    try:
                        east = self.maze[pos[0] + 1][pos[1]]
                        if not east.getIsVisited():
                            self.maze[pos[0]][pos[1]].setE(True)
                            self.maze[pos[0]][pos[1]].setIsVisited(True)
                            self.setCurrPos([pos[0] + 1, pos[1]])
                            return self.carve([self.getCurrPos()[0], self.getCurrPos()[1]])
                    except IndexError:
                        continue
                    # finally:
                    #     print(["E", pos[0] + 1, pos[1]])

                return self.carve([self.getRandCoord(), self.getRandCoord()])

            if card == "W":
                if 0 <= pos[0] - 1 < self.size:
                    try:
                        west = self.maze[pos[0] + 1][pos[1]]
                        if not west.getIsVisited():
                            self.maze[pos[0]][pos[1]].setW(False)
                            self.maze[pos[0]][pos[1]].setIsVisited(True)
                            self.setCurrPos([pos[0] - 1, pos[1]])

                            return self.carve([self.getCurrPos()[0], self.getCurrPos()[1]])
                    except IndexError:
                        continue
                    # finally:
                    #     print(["W", pos[0] - 1, pos[1]])

                return self.carve([self.getRandCoord(), self.getRandCoord()])
        return self.printBoard(True)

    def printBoard(self, depth=None):
        if depth:
            m = []
            for i in range(self.size):
                m.append([])
                for j in range(self.size):
                    m[i].append([])
                    if self.maze[i][j].getIsVisited():
                        m[i][j] = True
                    else:
                        m[i][j] = False
            for row in m:
                print(row)
            return

        for row in maze.maze:
            print(row)


size = int(input('Input a integer: '))
maze = Maze(size)
start = [maze.getRandCoord(), maze.getRandCoord()]  # start[X,Y]
# print(start, end)
maze.carve([0, 0])
# print(maze.maze[2][9])
