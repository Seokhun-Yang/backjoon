numOfLine = int(input())
overAverScores = {}
dic = {}

for n in range(numOfLine):
    dic[n] = list(map(int, input().split()))

for key, value in dic.items():
    sumOfNum = 0

    for s in value:
        sumOfNum += s

    average = sumOfNum // value[0]
    newDic = {}
    newList = []

    for s in value:
        if average <= s:
            newList.append(s)

    newDic[value[0]] = newList
    overAverScores[key] = newDic

for key, value in overAverScores.items():
    for k, v in value.items():
        print("%0.3f%%" % (len(v) / k * 100))
