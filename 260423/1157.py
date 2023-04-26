inputValue = input().lower()

mostAppearValue = ""
appearTime = 0
newDic = {}
boolean = bool()

for value in inputValue:
    if value in newDic:
        newDic[value] = newDic.get(value) + 1
    else:
        newDic[value] = 1

sortedDic = sorted(newDic.items(), key=lambda x: x[1], reverse=True)

for key, value in sortedDic:
    if appearTime < value:
        appearTime = value
        mostAppearValue = key
    elif appearTime == value:
        boolean = True

if boolean:
    print("?")
else:
    print(mostAppearValue.upper())
