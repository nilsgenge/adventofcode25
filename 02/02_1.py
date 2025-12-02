
res = 0

with open("input", "r") as file:
    ranges = file.read().split(",")

def checkIfValid(id: int):
    if len(str(id)) % 2 == 1:
        return True

    mid = len(str(id)) // 2
    a = int(str(id)[:mid])
    b = int(str(id)[mid:])

    return a != b


for r in ranges:
    low = int(r.split("-")[0])
    high = int(r.split("-")[1])
    for id in range(low, high+1):
        if not checkIfValid(id):
            res += id

print(res)

