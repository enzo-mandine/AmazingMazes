from re import split
from PIL import Image


class MazeSolver:

    def __init__(self):

        self.nodes = None
        self.edges = None
        self.draw = None
        self.weight = None
        self.path = []
        self.end = None

        self.setup()
        self.weight_graph()

    def setup(self):
        file = open('../maze2.mz', 'r')
        read = file.read()
        file.close()
        lab = split(r"\n", read)

        draw = []
        for row in lab:
            if len(row) > 0:
                draw.append(list(row))

        m = []
        for i in range(len(draw)):
            m.append([])
            for j in range(len(draw[0])):
                m[i].append(0)

        m[0][0] = 1
        self.weight = m
        self.draw = draw
        self.end = (len(self.weight) - 1, len(self.weight[0]) - 1)
        self.path.append(self.end)

    def weight_graph(self):
        k = 0
        while self.weight[-1][-1] == 0:
            k += 1
            for i in range(len(self.weight)):
                for j in range(len(self.weight[i])):
                    if int(self.weight[i][j]) == k:
                        if i > 0 and self.weight[i - 1][j] == 0 and self.draw[i - 1][j] == ".":
                            self.weight[i - 1][j] = k + 1
                        if j > 0 and self.weight[i][j - 1] == 0 and self.draw[i][j - 1] == ".":
                            self.weight[i][j - 1] = k + 1
                        if i < len(self.weight) - 1 and self.weight[i + 1][j] == 0 and self.draw[i + 1][j] == ".":
                            self.weight[i + 1][j] = k + 1
                        if j < len(self.weight[i]) - 1 and self.weight[i][j + 1] == 0 and self.draw[i][j + 1] == ".":
                            self.weight[i][j + 1] = k + 1

    def get_path(self):
        y, x = self.end
        while self.weight[-1][-1] > 1:

            if y > 0 and self.weight[y - 1][x] == self.weight[-1][-1] - 1:
                y, x = y - 1, x
                self.path.append((y, x))
                self.weight[-1][-1] -= 1
            elif x > 0 and self.weight[y][x - 1] == self.weight[-1][-1] - 1:
                y, x = y, x - 1
                self.path.append((y, x))
                self.weight[-1][-1] -= 1
            elif y < len(self.weight) - 1 and self.weight[y + 1][x] == self.weight[-1][-1] - 1:
                y, x = y + 1, x
                self.path.append((y, x))
                self.weight[-1][-1] -= 1
            elif x < len(self.weight[y]) - 1 and self.weight[y][x + 1] == self.weight[-1][-1] - 1:
                y, x = y, x + 1
                self.path.append((y, x))
                self.weight[-1][-1] -= 1

        return self.path

    def get_png(self):
        self.get_path()
        for i in range(0, len(self.weight)):
            for j in range(0, len(self.weight[0])):
                if self.weight[i][j] != 0:
                    self.draw[i][j] = "*"
                if (i, j) in self.path:
                    self.draw[i][j] = 'o'

        pil_data = []
        for i in range(0, len(self.draw)):
            for j in range(0, len(self.draw[i])):
                if self.draw[i][j] == 'o':
                    pil_data.append((255, 0, 255))
                if self.draw[i][j] == '#':
                    pil_data.append((0, 0, 0))
                if self.draw[i][j] == '.':
                    pil_data.append((255, 255, 255))
                if self.draw[i][j] == '*':
                    pil_data.append((0, 0, 255))

        image = Image.new('RGB', (len(self.draw), len(self.draw[0])))
        image.putdata(pil_data)

        file_name = ""
        while file_name == "":
            file_name = str(input('Choisissez un nom de fichier:'))

        image.save(file_name + '.png')


solver = MazeSolver()
solver.get_png()
