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
        for y in range(0, self.size):
            matrix.append([])
            for x in range(0, self.size):
                room = Room(y, x, idx)
                matrix[y].append(room)
                idx += 1
        self.matrix = matrix

        return True

    def resolve(self):
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
    # end Matrix


class Room:
    def __init__(self, y, x, idx):
        self.x = y
        self.y = x
        self.idx = idx
        self.neighbours = None
        self.isWall = {'n': True, 's': True, 'e': True, 'w': True}

    def openWall(self, position):
        if position == (self.x, self.y - 1):
            self.isWall['n'] = False
        if position == (self.x, self.y + 1):
            self.isWall['s'] = False
        if position == (self.x + 1, self.y):
            self.isWall['e'] = False
        if position == (self.x - 1, self.y):
            self.isWall['w'] = False

    def getPosition(self):
        return self.x, self.y
    # end Room


size = int(input('dimension:'))
matrix = Matrix(size)
matrix.resolve()
print'walls:', matrix.allWalls
