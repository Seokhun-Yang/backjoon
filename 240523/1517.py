import sys

times = sys.stdin.readline().rstrip()
numList = list(map(int, sys.stdin.readline().rstrip().split()))
count = 0

for _ in range(len(numList) - 1):
    for i in range(len(numList) - 1):
        if numList[i] > numList[i + 1]:
            count += 1
            temp = numList[i]
            numList[i] = numList[i + 1]
            numList[i + 1] = temp

print(count)
