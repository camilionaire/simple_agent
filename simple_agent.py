
import random

def placeDirt(n):
    dirt_clops = n
    clean_grid = [[True, True, True],
            [True, True, True],
            [True, True, True]]


    # for i in clean_grid:
    #     for j in i:
    #         print(j, end= " ")
    #     print()

    # print("\nRandomizing", dirt_clops, "dirt piles \n")

    random.seed()

    while dirt_clops > 0:
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        if clean_grid[i][j] == True:
            clean_grid[i][j] = False
            dirt_clops = dirt_clops - 1

    return clean_grid

def placeAgent():
    i = random.randint(0, 2)
    j = random.randint(0, 2)
    return [i, j]

def checkGrid(grid):
    for i in grid:
        for j in i:
            if j == False:
                return False

    return True

def randomMove(grid, loc):
    moved = False
    while not moved:
        choice = random.randint(0, 5)

        if choice == 0: # No op
            moved = True
        elif choice == 1: # Suck
            if grid[loc[0]][loc[1]] == False:
                grid[loc[0]][loc[1]] = True
            moved = True
        elif choice == 2: #move left
            if loc[1] != 0:
                loc[1] = loc[1] - 1
                moved = True
        elif choice == 3: # move right
            if loc[1] != 2:
                loc[1] = loc[1] + 1
                moved = True
        elif choice == 4: #move up
            if loc[0] != 0:
                loc[0] = loc[0] - 1
                moved = True
        elif choice == 5: # move down
            if loc[0] != 2:
                loc[0] = loc[0] + 1
                moved = True

    return grid, loc

def randomMurpheys(grid, loc):
    moved = False
    while not moved:
        choice = random.randint(0, 5)

        if choice == 0: # No op
            moved = True
        elif choice == 1: # Suck
            # if grid[loc[0]][loc[1]] == False:
            if 0 != random.randint(0, 4):
                grid[loc[0]][loc[1]] = True
            else:
                grid[loc[0]][loc[1]] = False
            moved = True
        elif choice == 2: #move left
            if loc[1] != 0:
                loc[1] = loc[1] - 1
                moved = True
        elif choice == 3: # move right
            if loc[1] != 2:
                loc[1] = loc[1] + 1
                moved = True
        elif choice == 4: #move up
            if loc[0] != 0:
                loc[0] = loc[0] - 1
                moved = True
        elif choice == 5: # move down
            if loc[0] != 2:
                loc[0] = loc[0] + 1
                moved = True

    return grid, loc

def simulation_rando():
    clean_grid = placeDirt(1)
    agent_loc = placeAgent()

    moves = 0

    while not checkGrid(clean_grid):
        clean_grid, agent_loc = randomMurpheys(clean_grid, agent_loc)
        moves = moves + 1

    return moves

def reflex(grid, loc):
    if grid[loc[0]][loc[1]] == False:
       grid[loc[0]][loc[1]] = True
       return grid, loc, 1
    else:
        if loc[0] == 0:
            if loc[1] != 2:
                loc[1] = loc[1] + 1
                return grid, loc, 1
            else:
                loc[0] = loc[0] + 1
                return grid, loc, 1
        elif loc[0] == 1:
            if loc[1] != 0:
                loc[1] = loc[1] - 1
                return grid, loc, 1
            else:
                loc[0] = loc[0] + 1
                return grid, loc, 1
        elif loc[0] == 2:
            if loc[1] == 2:
                return grid, [0, 0], 4 #moves 2 left, 2 up
            else:
                loc[1] = loc[1] + 1
                return grid, loc, 1

def reflexMurpheys(grid, loc):
    if grid[loc[0]][loc[1]] == False:
       grid[loc[0]][loc[1]] = True
       return grid, loc, 1
    else:
        if loc[0] == 0:
            if loc[1] != 2:
                loc[1] = loc[1] + 1
                return grid, loc, 1
            else:
                loc[0] = loc[0] + 1
                return grid, loc, 1
        elif loc[0] == 1:
            if loc[1] != 0:
                loc[1] = loc[1] - 1
                return grid, loc, 1
            else:
                loc[0] = loc[0] + 1
                return grid, loc, 1
        elif loc[0] == 2:
            if loc[1] == 2:
                return grid, [0, 0], 4 #moves 2 left, 2 up
            else:
                loc[1] = loc[1] + 1
                return grid, loc, 1

def simulation_reflex():
    clean_grid = placeDirt(5)
    agent_loc = placeAgent()
    moves = 0

    while not checkGrid(clean_grid):
        clean_grid, agent_loc, nummov = reflex(clean_grid, agent_loc)
        moves = moves + nummov

    return moves
            
if __name__ == "__main__":
    total = 0
    for i in range(0, 10000):
        total = total + simulation_rando()
    avg = total / 10000
    print(avg)