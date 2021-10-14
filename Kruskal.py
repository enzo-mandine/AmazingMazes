from random import shuffle
import sys

sys.setrecursionlimit(15000)


# Improvement : merge print method :'(


class Room:
    """ A room of the maze with a position and 4 walls opened by default """

    def __init__(self, y: int, x: int, size: int):
        self.y = y
        self.x = x
        self.size = size
        self.neighbours = []
        self.is_visited = False
        self.isWall = {'n': False, 's': False, 'e': False, 'w': False}
        self.value = 0

        self.set_neighbours()

    def set_neighbours(self) -> None:
        """ push available neighbours position to attribute """

        y = self.y
        x = self.x
        neighbours = []
        size = range(self.size)
        N, S, E, W = y + 1, y - 1, x + 1, x - 1

        if N in size:
            neighbours.append((N, x))
        if S in size:
            neighbours.append((S, x))
        if E in size:
            neighbours.append((y, E))
        if W in size:
            neighbours.append((y, W))

        self.neighbours = neighbours

        return None

    def close_wall(self, position: tuple or list) -> None:
        """ given a position, close the corresponding wall """

        if position == (self.y - 1, self.x):
            self.isWall['n'] = True
        if position == (self.y + 1, self.x):
            self.isWall['s'] = True
        if position == (self.y, self.x + 1):
            self.isWall['e'] = True
        if position == (self.y, self.x - 1):
            self.isWall['w'] = True

        return None

    def get_position(self) -> tuple:
        """ return (y,x) of a room """

        return self.y, self.x
    # end Room


class Labyrinth:
    """ The labyrinth, 2D array composed of Room object """

    def __init__(self, size: int):
        # init vars
        self.size = size
        self.matrix = None
        self.rooms_sets = None
        self.all_walls = None

        # backtracking draw
        self.horizontal = None
        self.vertical = None

        # fill the maze with room object
        self._set_matrix()
        self._choose_engine()

    def _choose_engine(self) -> None:
        print('select your maze engine:\n1: Backtracking\n2: Kruskal')
        engine = int(input(''))

        if engine == 1:
            self._build_backtracking_maze(0, 0)
            self._print_backtracking_maze()
        if engine == 2:
            self._build_kruskal_maze()
            self._print_kruskal_maze()

        return None

    def _run_kruskal_setup(self) -> None:
        """ run needed setups for kruskal generation """

        self._set_all_rooms_sets()
        self._set_all_walls()

        return None

    def _set_matrix(self) -> None:
        """ Create a matrix and fill it with Room Objects and store it in attribute """

        matrix = []
        for row in range(0, self.size):
            matrix.append([])
            for col in range(0, self.size):
                room = Room(row, col, self.size)
                matrix[row].append(room)
        self.matrix = matrix

        return None

    def _set_all_rooms_sets(self) -> None:
        """ for each cell in the matrix, create a set (x,y) and store them in an attribute """

        allRooms = [{(x, y)}
                    for x in range(self.size)
                    for y in range(self.size)]
        self.rooms_sets = allRooms

        return None

    def _set_all_walls(self) -> None:
        """ for each cell in the matrix, create a set of wall connecting cells like: (0,0,0,1) """

        walls = [(x, y, x + 1, y)
                 for x in range(self.size - 1)
                 for y in range(self.size)]
        walls.extend([(x, y, x, y + 1)
                      for x in range(self.size)
                      for y in range(self.size - 1)])
        self.all_walls = walls

        return None

    def _get_room(self, pos: list or tuple) -> Room:
        """ retrieve a room in the matrix from given (y,x) """

        return self.matrix[pos[0]][pos[1]]

    def _set_all_rooms_walls(self) -> None:
        """ for each wall left, open it in the corresponding Room """

        for wall in self.all_walls:
            a = self._get_room((wall[0], wall[1]))
            b = self._get_room((wall[2], wall[3]))
            a.close_wall(b.get_position())
            b.close_wall(a.get_position())

        return None

    def _build_backtracking_maze(self, y: int, x: int) -> bool:
        if not self.horizontal and not self.vertical:
            self.horizontal = [["###"] * self.size + ['#'] for _ in range(self.size + 1)]
            self.vertical = [["#.."] * self.size + ['#'] for _ in range(self.size)] + [[]]

        room = self._get_room((y, x))
        room.is_visited = True

        d = room.neighbours
        shuffle(d)

        for (yy, xx) in d:
            room_n = self._get_room((yy, xx))
            if room_n.is_visited:
                continue

            if xx == x:
                self.horizontal[max(y, yy)][x] = "#.."
            if yy == y:
                self.vertical[y][max(x, xx)] = "..."
            # room_n.isWall['n'] = True

            self._build_backtracking_maze(yy, xx)

        return True

    def _print_backtracking_maze(self) -> None:
        self.vertical[0][0] = '...'
        self.vertical[-2][-1] = '.'
        self.horizontal[0][0] = '..#'
        self.horizontal[-1][-1] = '.'
        self.horizontal[-1][-2] = '##.'
        s = ""
        for (a, b) in zip(self.horizontal, self.vertical):
            s += ''.join(a + ['\n'] + b + ['\n'])
        print(s)

        return None

    def _build_kruskal_maze(self) -> bool:
        """ build the maze with Kruskal """

        # Run setup
        self._run_kruskal_setup()

        # get al the walls possible in the maze
        walls_copy = self.all_walls[:]

        # shuffle them to add randomness
        shuffle(walls_copy)

        # loop over each possible wall
        for wall in walls_copy:
            set_a = None
            set_b = None

            # loop over each cell sets
            for s in self.rooms_sets:

                # if we find x,y in one of the set
                if (wall[0], wall[1]) in s:
                    # make a set
                    set_a = s

                # same here
                if (wall[2], wall[3]) in s:
                    set_b = s

            # if sets are disjointed
            if set_a is not set_b:
                # remove the existing sets
                self.rooms_sets.remove(set_a)
                self.rooms_sets.remove(set_b)

                # merge them
                self.rooms_sets.append(set_a.union(set_b))
                # make a path
                self.all_walls.remove(wall)

        # once we are done, setup all the object in the matrix for printing
        self._set_all_rooms_walls()

        return True

    def _print_kruskal_maze(self) -> None:
        """ print the maze, '#'/'##' for wall, '..' for path """

        vertical = [["###"] * dimension + ['#'] for _ in range(self.size + 1)]
        horizontal = [["#.."] * dimension + ['#'] for _ in range(self.size)] + [[]]

        for i in range(self.size):
            for j in range(self.size):
                room = self.matrix[i][j]
                walls = room.isWall

                if not walls["n"]:
                    vertical[i][j] = "#.."
                if not walls["w"]:
                    horizontal[i][j] = "..."

        # Setup first row and opening
        vertical[0] = ['...' + ('###' * (dimension - 1)) + '#']
        s = ""
        for i in horizontal:
            for j in range(0, len(i) - 1):
                horizontal[j][0] = '#..'

        # Open start and end
        horizontal[0][0] = '...'
        horizontal[-2][-1] = '.'
        vertical[-1][-2] = '#..'
        vertical[-1][-1] = '.'

        # print a string block
        for (a, b) in zip(vertical, horizontal):
            s += ''.join(a + ['\n'] + b + ['\n'])
        print(s)

        return None
    # end Matrix


dimension = 0
while dimension < 2:
    dimension = int(input('size:'))
    if dimension < 2:
        print('maze must be at least 2*2 :(\n')

maze = Labyrinth(dimension)

print(maze.matrix[0][0].neighbours)
