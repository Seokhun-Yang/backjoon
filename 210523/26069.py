import sys

newList = []
peopleWhoDance = ["ChongChong"]

for _ in range(int(sys.stdin.readline().rstrip())):
    a, b = sys.stdin.readline().rstrip().split()
    newList.append([a, b])

for value in newList:
    a, b = value[0], value[1]

    if a in peopleWhoDance and b not in peopleWhoDance:
        peopleWhoDance.append(b)
    elif b in peopleWhoDance and a not in peopleWhoDance:
        peopleWhoDance.append(a)

print(len(peopleWhoDance))
