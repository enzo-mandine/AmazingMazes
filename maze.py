size = 6
maze = [["'","#",'#',"'","#","'"],
        ["'","'","'","'","#","'"],
        ["#","'","'","#","'","'"],
        ["'","#","'","#","'","#"],
        ["'","#","'","'","'","'"],
        ["'","'","#","'","#","'"]
]

#Creer une liste pour stocker la reponse
solution = [["#"]* size for i in range(size)]

#D"finir la fonction qui contient l'algorithme
def solveMaze(row,col):

#Si la cellule courante est la cellule de destination, le puzzle est résolu
    if (row == size-1) and (col == size -1):
        solution[row][col] = "."
        return True

# Sinon, verifier si la case est appropriée pour le premier mouvement, la case doit être dans le rang (0,size-1),
# puis , on doit voir si elle n'est pas deja visifté et si elle n'est pas bloquée

    if row>=0 and col>=0 and row<size and col< size and solution[row][col]== "#" and maze[row][col] == "'":
        solution[row][col] = "."
    # on va  à la case en bas
        if solveMaze(row+1, col):
            return True
    # on va vers la droite
        if solveMaze(row, col+1):
            return True
    #on va vers le haut
        if solveMaze(row -1, col):
            return True
    # on va vers la gauche
        if solveMaze(row , col-1):
            return True
    # Si aucune de ces options n'est valide on retourne à la case precedante
        solution[row][col] = "#"
        return False
    return 0

# Lancer le jeu
if solveMaze(0,0):
    for i in solution:
        print(i)
else :
    print("Il n'y a pas de solution")
