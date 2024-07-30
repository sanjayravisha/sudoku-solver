# opens input file and output file
input_file = open("sudoku.in")
output_file = open("sudoku.out", "w")

# defines global variables
dimensions = 9
board = [[0 for row in range(dimensions)] for col in range(dimensions)]

# overlays given board onto board
for row in range(dimensions):
    line = input_file.readline()
    for col in range(dimensions):
        num = line[2*col]
        board[row][col] = int(num)

# recursive function to help solve sudoku board
def solve(board):

    # checks if there are empty squares
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    # tries numbers into first empty square
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            # checks if there are any empty squares
            if solve(board):
                return True
            board[row][col] = 0
    return False

# 
def valid(bo, num, pos):
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[1]//3
    box_y = pos[0]//3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and pos != (i, j):
                return False
    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None

print_board(board)
solve(board)
print("_________________________")
print("")
print_board(board)