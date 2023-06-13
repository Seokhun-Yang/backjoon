import sys

numGreetings = 0
nameDic = {}

for _ in range(int(sys.stdin.readline().rstrip())):
    i = sys.stdin.readline().rstrip()

    if i == "ENTER":
        numGreetings += len(nameDic)
        nameDic.clear()
        continue

    if i in nameDic:
        nameDic[i] += 1
        continue

    nameDic[i] = 1

print(numGreetings + len(nameDic))
