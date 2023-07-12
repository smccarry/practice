# VARIABLES:
grid = [0, 0, 0, 0, 0, 0, 0, 0, 0]
list_check = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [3, 5, 7], [1, 5, 9]]

turnLimit = 0
over = False


# FUNCTIONS:

# function to print the grid:
def print_grid():
    b = 0
    for row in range(3):
        for column in range(3):
            print(grid[b], end="")
            b += 1
        print()


# checks whether someone has won from their move:
def check():
    win = False

    # for loop going through list of winning patterns:
    for a in list_check:
        if grid[a[0] - 1] == grid[a[1] - 1] and grid[a[0] - 1] == grid[a[2] - 1] and grid[a[0] - 1] != 0:
            print("YOU WON")
            win = True
            break

    return win


# THE MAIN LOOP:
print_grid()
while over is False:

    # CHECKING TURN LIMIT:
    if turnLimit >= 9 or over:
        print("TIE!!")
        break

    # PLAYER 1:
    coord = int(input("Player 1:")) - 1
    if grid[coord] == 0:
        grid[coord] = 1
    else:
        while grid[coord] != 0:
            coord = int(input("That space is filled. Try again.")) - 1
            if grid[coord] == 0:
                grid[coord] = 1
                break

    print_grid()

    if check():
        print("player 1 won!")
        break
    turnLimit += 1

    # PLAYER 2:
    coord = int(input("Player 2:")) - 1
    if grid[coord] == 0:
        grid[coord] = 2
    else:
        while grid[coord] != 0:
            coord = int(input("That space is filled. Try again.")) - 1
            if grid[coord] == 0:
                grid[coord] = 2
                break

    print_grid()

    if check():
        print("player 2 won!")
        break

    turnLimit += 1
