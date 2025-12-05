
accessible_rolls = 0

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


for y,row in enumerate(rolls):
    for x, column in enumerate(row):
        if rolls[y][x] == '@':
            if getNumNearbyRolls(y,x) < 4:
                accessible_rolls += 1


print("Accessible rolls: " + str(accessible_rolls))


