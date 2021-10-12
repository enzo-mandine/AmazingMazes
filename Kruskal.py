import random


class Matrix:
    def __init__(self, size):
        self.size = size
        self.matrix = None
        self.allRooms = None
        self.allWalls = None
        self.allRoomsObjects = []

        self._setMatrix()
        self._setAllRooms()
        self._setAllWalls()

        self._resolve()

    def printMaze(self):
        horizontal = [["####"] * size + ['#'] for _ in range(self.size + 1)]
        vertical = [["#..."] * size + ['#'] for _ in range(self.size)] + [[]]

        for i in range(self.size):
            for j in range(self.size):
                room = self.matrix[i][j]
                walls = room.isWall
                if walls["n"]:
                    horizontal[i][j] = "####"
                else:
                    horizontal[i][j] = "#..."
                if not walls["w"]:
                    vertical[i][j] = "...."
                else:
                    vertical[i][j] = "#..."

        # Setup first row
        horizontal[0] = ['..##' + ('####' * (size - 1)) + '#']
        s = ""
        for i in vertical:
            for j in range(0, len(i) - 1):
                vertical[j][0] = '#...'

        # Open start and end
        vertical[0][0] = '....'
        vertical[-2][-1] = '.'
        horizontal[-1][-2] = '###.'
        horizontal[-1][-1] = '.'

        # print on string block
        for (a, b) in zip(horizontal, vertical):
            s += ''.join(a + ['\n'] + b + ['\n'])
        print s

    def _setRoomWalls(self):
        for wall in self.allWalls:
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
        for row in range(0, self.size):
            matrix.append([])
            for col in range(0, self.size):
                room = Room(row, col)
                matrix[row].append(room)
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
    def __init__(self, y, x):
        self.y = y
        self.x = x
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

matrix.printMaze()

# for row in matrix.matrix:
#     for col in row:
#         print col.getPosition(), col.isWall
# print'walls:', matrix.allWalls
# print'rooms:', matrix.allRooms
# print'matrix:', matrix.matrix
