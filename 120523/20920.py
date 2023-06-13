import sys


def get_len(key):
    return len(key[0])


a, b = sys.stdin.readline().rstrip().split()
wordList = [sys.stdin.readline().rstrip() for _ in range(int(a))]
dic = {}

for word in wordList:
    if word in dic:
        dic[word] = dic[word] + 1
        continue

    dic[word] = 1

result = []
finalDic = sorted(
    sorted(sorted(dic.items()), key=get_len, reverse=True),
    key=lambda x: x[1], reverse=True)

for k, v in finalDic:
    if len(k) >= int(b):
        result.append(k)

for w in result:
    print(w)
