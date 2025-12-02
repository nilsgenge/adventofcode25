
res = 0

with open("input", "r") as file:
    ranges = file.read().split(",")

def checkIfValid(id: int) -> bool:
    s = str(id)
    length = len(s)

    for i in range(1, length):
        if(length % i == 0):
            part = s[:i]
            if part*(length // i) == s:
                return False
    return True




for r in ranges:
    low_s, high_s = r.split("-")
    low = int(low_s)
    high = int(high_s)
    for id in range(low, high+1):
        if not checkIfValid(id):
            res += id
            print("INVALID: " + str(id))

print("RESULT: " + str(res))

