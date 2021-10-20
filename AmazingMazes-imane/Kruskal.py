
from random import choice
# Definir la class avec largeur et longeur comme attributs
class Maze:
    def __init__(self,width,height):
        self.width = width
        self.height = height

# Stocker les cases dans une liste

        self.cells = []
        counter = 1
        for h in range(self.height):
            self.cells.append([])
            for w in range(self.width):
                self.cells[h].append(counter)
                counter += 1

# Stocker les bords dans un dictionnaire avec leur statut

        self.edges = dict()
        for h in range(self.height):
            for w in range(self.width):
                if w < self.width - 1:
                    self.edges[((w,h),(w+1,h))] = True
                if h < self.height - 1:
                    self.edges[((w,h),(w,h+1))] = True

# Compter le nombre de mouvement necessaire pour finir le jeu

        self.steps = 0
# Obtenir une case du gride

    def get_cell(self,cell):
        return self.cells[cell[1]][cell[0]]

# Stocker la case dans une variable

    def set_cell(self,cell,variable):
        self.cells[cell[1]][cell[0]] = variable

# Joindre les deux case connectées dans la même variable

    def apply_set(self,set_1,set_2):
        for w in range(self.width):
            for h in range(self.height):
                if self.get_cell((w,h)) == set_2:
                    self.set_cell((w,h),set_1)

# Verifier si deux cases sont connectées

    def is_connected(self,cell_1,cell_2):
        return self.get_cell(cell_1) == self.get_cell(cell_2)

# Définir si la case est appropriée

    def is_valid(self):
        s = self.get_cell((0,0))
        for w in range(self.width):
            for h in range(self.height):
                if self.get_cell((w,h)) != s:
                    return False
        return True
# Choisir un bord au hasard, le detruire et le stocker dans la liste "utilisé" si les deux cases concernés sont connectés et on compte le nombre des étapes

    def generate_maze(self):
        used_edges = []
        while not self.is_valid():
            edge = choice(list(set(self.edges.keys()) - set(used_edges)))
            used_edges.append(edge)
            if not self.is_connected(edge[0],edge[1]):
                self.edges[edge] = False
                self.apply_set(self.get_cell(edge[0]),self.get_cell(edge[1]))

            self.steps += 1

# Définir la fonction qui va imprimer la forme de la labyrinte

    def __str__(self):
        display = []
        for h in range(2 * self.height - 1):
            display.append([])
            for w in range(2 * self.width - 1):
                if (w % 2 == 1) and (h % 2 == 1):
                    display[h].append('#')
                elif (w % 2 == 1) and (h % 2 == 0) and self.edges[(((w - 1)/2 , h/2),((w + 1)/2, h/2))] :
                    display[h].append('#')
                elif (w % 2 == 0) and (h % 2 == 1) and self.edges[((w/2,(h - 1)/2), (w/2,(h+1)/2))]:
                    display[h].append("###")
                else:
                    if w % 2 == 0:
                        if h % 2 == 0 and w/2 == self.width - 1 and h/2 == self.height -1:
                            display[h].append("...")
                        elif h % 2 == 0 and w/2 == 0 and h/2 == 0:
                            display[h].append("...")
                        else :
                            display[h].append("...")
                    else:
                        display[h].append(".")

        for i in range(len(display)):
            display[i] = "".join(["#"] + display[i] + ["#"])
        return "\n".join([".." + ("#" * (4 * self.width - 1)) + " "] + display + ["" + ("#" * (4 * self.width - 1)) + ".."])

# Demander de renseigner les dimensions
width = int(input("Choose the width of the maze "))
height = int(input("Choose the height of the maze "))


# Création d'un objet à l'aide de la classe Maze et l'imprimer
maze = Maze(width,height)
maze.generate_maze()


print("Number of moves used to solve the maze: ", maze.steps)
print(maze)





















