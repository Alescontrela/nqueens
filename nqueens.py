import copy # copy board solutions into `solutions` var

def initialize(n, board): # initialize the board
    for key in ['queen','row','col','nwtose','swtone']:
        board[key] = {}

    for i in range(n): # set the queen positions, row vals, and col vals to empty
        board['queen'][i] = -1
        board['row'][i] = 0
        board['col'][i] = 0

    for i in range(-(n-1), n): # set main diagonal to empty
        board['nwtose'][i] = 0

    for i in range(2*n-1): # set opposite diagonal to empty
        board['swtone'][i] = 0

def is_free(i, j, board): # function to check whether a spot is available
    return(board['row'][i]==0 and board['col'][j]==0 and board['nwtose'][j-i]==0 and board['swtone'][j+i]==0)

def addqueen(i,j,board): # add a queen by filling the spot
    board['queen'][i] = j
    board['row'][i] = -1
    board['col'][j] = -1
    board['nwtose'][j-i] = -1
    board['swtone'][j+i] = -1

def undoqueen(i,j,board): # undo the filling of a spot
    board['queen'][i] = -1
    board['row'][i] = 0
    board['col'][j] = 0
    board['nwtose'][j-i] = 0
    board['swtone'][j+i] = 0

def add_solution(board): # save a solution
    global solutions
    saved_board = copy.deepcopy(board)
    solutions.append(saved_board)

def placequeen(i, board):
    n = len(board['queen'].keys()) # number of columns

    for j in range(n): # loop over all columns in the row
        if is_free(i, j, board):
            addqueen(i, j, board) # add queen is spot is free
            if i == n-1:  # if on last row, add the solution, remove the queen, and return
                add_solution(board)
                undoqueen(i,j,board)
                return
            placequeen(i+1, board) # add a queen to the next row

            undoqueen(i,j,board) # undo queen placement to find all solutions

def printsolutions(solutions, size, print_sol = True): # print the solutions
    num_solutions = len(solutions)
    if print_sol == True:
        print("{} solutions total".format(num_solutions))
    for sol in solutions:
        arr = [[0 for i in range(size)] for i in range(size)]
        for row in sorted(sol['queen'].keys()):
            arr[row][sol['queen'][row]] = 1
        if print_sol == True:
            print('\n'.join('{}'.format(k) for k in (arr)))
            print("---")
    return num_solutions

def take_input(): # take user input
    while True:
        try:
            size = int(input("Enter the size of the board: "))
            if size == 1:
                print("Arbitrary solution, enter a number that is at least 4")
            if size <= 3:
                print("Enter a number that is at least 4")
        except ValueError:
            print("Please enter numerical value")
        else:
            break

    return size

if __name__ == '__main__':
    solutions = []
    size = take_input()
    board = {}
    initialize(size, board)

    placequeen(0, board)

    printsolutions(solutions, size)
