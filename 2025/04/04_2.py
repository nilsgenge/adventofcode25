
removed_rolls = 0

with open("input", "r") as file:
    rolls = [list(line) for line in file.read().splitlines()]

last_row = len(rolls)-1
last_column = len(rolls[0])-1

def getNumNearbyRolls(y,x) -> int:
    numNeighbors = 0
    if y>0:
        numNeighbors += 1 if rolls[y-1][x] == "@" else 0
    if y<last_row:
        numNeighbors += 1 if rolls[y+1][x] == "@" else 0
    if x>0:
        numNeighbors += 1 if rolls[y][x-1] == "@" else 0
    if x<last_column:
        numNeighbors += 1 if rolls[y][x+1] == "@" else 0
    if y>0:
        if x>0:
            numNeighbors += 1 if rolls[y-1][x-1] == "@" else 0
        if x<last_column:
            numNeighbors += 1 if rolls[y-1][x+1] == "@" else 0
    if y<last_row:
        if x>0:
            numNeighbors += 1 if rolls[y+1][x-1] == "@" else 0
        if x<last_column:
            numNeighbors += 1 if rolls[y+1][x+1] == "@" else 0
    return numNeighbors

def getNumRemovableRolls() -> int:
    removableRolls = 0
    for y,row in enumerate(rolls):
        for x, column in enumerate(row):
            if rolls[y][x] == '@':
                if getNumNearbyRolls(y,x) < 4:
                    removableRolls += 1
    return removableRolls

def removeRolls() -> int:
    global rolls
    rollsCopy = [row.copy() for row in rolls]
    removableRolls = 0
    for y,row in enumerate(rollsCopy):
        for x, column in enumerate(row):
            if rollsCopy[y][x] == '@':
                if getNumNearbyRolls(y,x) < 4:
                    rollsCopy[y][x] = '.'
    rolls = rollsCopy
    return removableRolls


while getNumRemovableRolls() > 0:
    removed_rolls += getNumRemovableRolls()
    removeRolls()


print("Removed rolls: " + str(removed_rolls))


