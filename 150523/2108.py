import sys

numList = []
sumOfNum = 0

for _ in range(int(sys.stdin.readline().rstrip())):
    number = int(sys.stdin.readline().rstrip())
    numList.append(number)
    sumOfNum += number

numList.sort()

aver = round(sumOfNum / len(numList))
median = numList[round(len(numList) / 2)]
ran = numList[len(numList) - 1] - numList[0]

dic = {}

for num in numList:
    if num in dic:
        dic[num] = dic[num] + 1
        continue
    dic[num] = 1

sortedDic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
modeList = []

for k, v in sortedDic:
    for k2, v2 in sortedDic:
        if len(sortedDic) < 3:
            if v > v2:
                modeList.append(k)
                continue
        if k == k2 or k2 in modeList:
            continue
        if v == v2:
            modeList.append(k2)

modeList.sort()
mode = int

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
