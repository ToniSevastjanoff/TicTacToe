def check_rows(player_id):
    global grid
    row_complete = False

    # check horizontal
    for y in range(3):
        if grid[y][0] == player_id and grid[y][1] == player_id and grid[y][2] == player_id:
            row_complete = True

    # check vertical
    for x in range(3):
        if grid[0][x] == player_id and grid[1][x] == player_id and grid[2][x] == player_id:
            row_complete = True

    # check diagonal
    if grid[0][0] == player_id and grid[1][1] == player_id and grid[2][2] == player_id:
        row_complete = True

    if grid[2][0] == player_id and grid[1][1] == player_id and grid[0][2] == player_id:
        row_complete = True

    return row_complete


def check_grid_filled():
    global grid
    is_grid_filled = True
    for y in range(3):
        for x in range(3):
            if grid[y][x] == "_":
                is_grid_filled = False
    return is_grid_filled


def check_impossible():
    global grid
    is_impossible = False
    x_wins = check_rows("X")
    o_wins = check_rows("O")
    if x_wins and o_wins:
        is_impossible = True

    # check amount of crosses and circles
    x_amount = [item for sublist in grid for item in sublist].count("X")
    o_amount = [item for sublist in grid for item in sublist].count("O")

    if abs(x_amount - o_amount) > 1:
        is_impossible = True
    return is_impossible


def update_cell(x, y, player_id):
    global grid
    x -= 1
    y -= 1
    # check if cell is already occupied
    if grid[x][y] != "_":
        print("This cell is occupied! Choose another one!")
        return False
    else:
        grid[x][y] = player_id
        return True


def print_grid():
    global grid
    print("---------")
    for y in range(3):
        print("| ", end='')
        for x in range(3):
            print(grid[y][x] + " ", end='')
        print("|")
    print("---------")


# start of program
grid = [["_" for j in range(3)] for i in range(3)]
player = "X"
X_wins = False
O_wins = False
grid_filled = False


# main loop
while not X_wins and not O_wins and not grid_filled:

    print_grid()

    grid_filled = check_grid_filled()
    X_wins = check_rows("X")
    O_wins = check_rows("O")
    impossible = check_impossible()

    if impossible:
        print("Impossible")
    elif X_wins:  # check if x has rows
        print("X wins")
        break
    elif O_wins:  # check if o has rows
        print("O wins")
        break
    elif grid_filled:
        print("Draw")
        break

    # input player move
    x_coord = 0
    y_coord = 0
    cell_updated = False

    while type(x_coord) != int or type(
            y_coord) != int or not 1 <= x_coord <= 3 or not 1 <= y_coord <= 3 or not cell_updated:
        x_coord, y_coord = input("Enter the coordinates:").split()

        if not x_coord.isnumeric() or not y_coord.isnumeric():
            print("You should enter numbers!")
        else:
            x_coord = int(x_coord)
            y_coord = int(y_coord)
            if not 1 <= x_coord <= 3 or not 1 <= y_coord <= 3:
                print("Coordinates should be from 1 to 3!")
            else:
                cell_updated = update_cell(x_coord, y_coord, player)

    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
