a, b = map(int, input().split())
intValues = list(map(int, input().split()))
result = 0

for first in intValues:
    for second in intValues:
        if first == second:
            continue

        for third in intValues:
            if third == first or third == second:
                continue

            sumValue = first + second + third

            if sumValue == result:
                continue

            if b >= sumValue > result:
                result = sumValue

print(result)
