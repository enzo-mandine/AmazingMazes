from random import shuffle, randrange

def make_maze(width,height):
    width = int(input('Choose the width of the maze '))
    height = int(input('Choose the height of the maze '))
    visited = [[0] * width + [1] for _ in range(height)] + [[1] * (width+1)]
    vertical = [["#.."] * width + ['#'] for _ in range(height)] + [[]]
    horizental = [["###"] * width + ['#'] for _ in range(height + 1)]
    vertical[0][0] = '...'
    horizental[-1][-1] = '.'


    def move(row,col):

        visited[col][row] = 1
        directions = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]
        shuffle(directions)
        for (Nrow, Ncol) in directions:
            if visited[Ncol][Nrow]: continue
            if Nrow == row: horizental[max(col, Ncol)][row] = "#.."
            if Ncol == col: vertical[col][max(row, Nrow)] = "..."

            move(Nrow, Ncol)

    move(randrange(width), randrange(height))


    string = ""
    for (a, b) in zip(horizental, vertical):
        string += ''.join(a + ['\n'] + b + ['\n'])
    return string



if __name__ == "__main__":
    print(make_maze(0,0))














