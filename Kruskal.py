import random


class Matrix:
    def __init__(self, size):
        self.size = size
        self.matrix = None
        self.allRooms = None
        self.allWalls = None

        self._setMatrix()
        self._setAllRooms()
        self._setAllWalls()

        self._resolve()

    def _setRoomWalls(self):
        for wall in self.allWalls:
            print(wall)
            a = self._getRoom((wall[0], wall[1]))
            b = self._getRoom((wall[2], wall[3]))
            a.openWall(b.getPosition())
            b.openWall(a.getPosition())

    def _getRoom(self, pos):
        return self.matrix[pos[0]][pos[1]]

    def _setAllWalls(self):
        walls = [(x, y, x + 1, y)
                 for x in range(self.size - 1)
                 for y in range(self.size)]
        walls.extend([(x, y, x, y + 1)
                      for x in range(self.size)
                      for y in range(self.size - 1)])
        self.allWalls = walls
        return True

    def _setAllRooms(self):
        allRooms = [{(x, y)}
                    for x in range(self.size)
                    for y in range(self.size)]
        self.allRooms = allRooms
        return True

    def _setMatrix(self):
        matrix = []
        idx = 0
        for row in range(0, self.size):
            matrix.append([])
            for col in range(0, self.size):
                room = Room(row, col, idx)
                matrix[row].append(room)
                idx += 1
        self.matrix = matrix

        return True

    def _resolve(self):
        walls_copy = self.allWalls[:]
        random.shuffle(walls_copy)

        for wall in walls_copy:
            set_a = None
            set_b = None

            for s in self.allRooms:
                if (wall[0], wall[1]) in s:
                    set_a = s
                if (wall[2], wall[3]) in s:
                    set_b = s

            if set_a is not set_b:
                self.allRooms.remove(set_a)
                self.allRooms.remove(set_b)
                self.allRooms.append(set_a.union(set_b))
                self.allWalls.remove(wall)

        self._setRoomWalls()
        return self
    # end Matrix


class Room:
    def __init__(self, y, x, idx):
        self.y = y
        self.x = x
        self.idx = idx
        self.neighbours = None
        self.isWall = {'n': False, 's': False, 'e': False, 'w': False}

    def openWall(self, position):
        if position == (self.y - 1, self.x):
            self.isWall['n'] = True
        if position == (self.y + 1, self.x):
            self.isWall['s'] = True
        if position == (self.y, self.x + 1):
            self.isWall['e'] = True
        if position == (self.y, self.x - 1):
            self.isWall['w'] = True
        return self

    def getPosition(self):
        return self.y, self.x
    # end Room


size = int(input('dimension:'))
matrix = Matrix(size)
for row in matrix.matrix:
    for col in row:
        print col.getPosition(), col.isWall
# print'walls:', matrix.allWalls
# print'rooms:', matrix.allRooms
