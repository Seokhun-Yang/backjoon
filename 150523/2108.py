import sys

non = int(sys.stdin.readline().rstrip())
numList = []
dic = {}
sumOfNum = 0

for _ in range(non):
    number = int(sys.stdin.readline().rstrip())
    numList.append(number)
    sumOfNum += number

    if number in dic:
        dic[number] = dic[number] + 1
        continue
    dic[number] = 1

numList.sort()
aver = round(sumOfNum / non)
median = numList[round(non / 2)]
ran = numList[non - 1] - numList[0]
sortedDic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
modeList = []
previousValue = None
pendingKey = 0
pendingValue = 0
numberOfMode = 0

for k, v in sortedDic:
    if previousValue is None:
        pendingKey = k
        pendingValue = v

    if previousValue == v:
        modeList.append(k)
        numberOfMode = v
        continue

    previousValue = v

if pendingValue == numberOfMode:
    modeList.append(pendingKey)

modeList.sort()
mode = 0

if len(modeList) == 1:
    mode = modeList[0]
elif len(modeList) > 1:
    mode = modeList[1]
else:
    mode = numList[0]

print(aver)
print(median)
print(mode)
print(ran)
