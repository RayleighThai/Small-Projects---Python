import random
from tabulate import tabulate #print array grid evenly *chef kiss*
import time # implement waiting time

# implement of time score can be start = clock() and end same way. with totaltimeinSec = score/Clock_per_sec

# Creation of mines pending on game difficulties
def gridCreation(col, row, mines):
    arr = [[0 for row in range(col)] for column in range(row)]
    randomBomb(arr, mines)
    checkArr(arr)
    return arr

# Randomize Bomb Placement
def randomBomb(arr, mines):
    for i in range(mines):
        bcol = random.randint(0,len(arr)-1)
        brow = random.randint(0,len(arr[0])-1)
        arr[bcol][brow] = 'X'

#check location for bomb
def checkArr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            # I know this is a Sin.... but I'll do it anyway
            if arr[i][j] == 0:
                count = 0
                num_rows, num_cols = len(arr), len(arr[0])
                #check neighbors for bomb(s)
                for x in range( (0 if i-1 < 0 else i-1), (num_rows if i+2 > num_rows else i+2), 1  ):
                    for y in range( (0 if j-1 < 0 else j-1), (num_cols if j+2 > num_cols else j+2), 1 ):
                        if arr[x][y] == "X":
                            count += 1
                arr[i][j] = count

# Generate Player Map and hide the Mines
def playerMapGenerator(col, row):
    arr = [["-" for row in range(col)] for column in range(row)]
    return arr

# Compare Player game progress completion
def gamecheck(arr):
    for row in arr:
        for cell in row:
            if cell == "-":
                return False
    return True

# Do player want to try again
def continueGameOrNot(score):
    end = time.time()
    score = end - score
    print("Your Score is : ", score )
    continueGame = input("Do you want to try again? (y/n) : ")
    if continueGame.lower() == "y":
        return True
    print("Thank you for Playing!")
    return False 

# Playing game process 
def playingGame(pgame, mgame, score, gameStatus, r, c):
    while True:
        if gamecheck(pgame) == False:
            print("\nSelect your cell:")
            print("Select your Column X (1 to ", c, "): ")
            x = int(input())-1
            print("Select your Row Y (1 to ", r, "): ")
            y = int(input())-1
            
            if (mgame[y][x] == "X" ):
                print("GAME OVER!")
                print(tabulate(mgame, tablefmt="pretty"))
                gameStatus = continueGameOrNot(score)
                break
            else:
                pgame[y][x] = mgame[y][x]
                print(tabulate(pgame, tablefmt="pretty"))
        else:
            print(tabulate(pgame))
            print("\t You WON!!! Congratulations!")
            gameStatus = continueGameOrNot(score)
            break
    return gameStatus

# Let the Game Begin
def game():
    print("\t Welcome to minesweeper")
    print("\nLevel of Difficulty: ")
    print(" 0 - Beginner (9x9) with 10 mines")
    print(" 1 - Intermediate (16x16) with 40 mines")
    print(" 2 - Hard (16x30) with 99 mines")
    print(" 3 - Extreme (24x30) with 180 mines")
    
    gameStatus = True
    while gameStatus:
        diff = input("Select your difficulty (1, 2, 3, 4): ")
        if diff == "1":
            col = 9 ; row = 9 ; mines = 10
        elif diff == "2":
            col =16 ; row = 16; mines = 40
        elif diff == "3":
            col =30; row = 16; mines = 99
        elif diff == "4":
            col =30; row = 24; mines = 180
        else:
            print("\n\nPlease enter level of difficulty listed above\nGame restarts in 5 Seconds\n")
            time.sleep(5)
            game()

        # Passing difficulty appropriate size and mines amounts
        minesweeperGame = gridCreation(col, row, mines)
        playergame = playerMapGenerator(col, row)
        score = time.time()
        gameStatus = playingGame(playergame, minesweeperGame, score, gameStatus, row, col)
        
if __name__ == "__main__":
    try:
        game()
    except KeyboardInterrupt:
        print("\nEnd of Game. Thank you for playing!\n")