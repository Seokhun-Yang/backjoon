inputValue = input()

origin = (1, 1, 2, 2, 2, 8)
valueList = inputValue.split(" ")
result = []

for i in range(len(valueList)):
    a = origin[i]
    result.append(a - int(valueList[i]))

for i in result:
    print(i, end=' ')
