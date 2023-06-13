import sys

numOfSquare = int(sys.stdin.readline().rstrip())
dic = {}
stackList = []

for i in range(numOfSquare):
    dic[i] = sys.stdin.readline().rstrip().split()


def getStackArea(a, b):
    a1, a2 = float(a[0]), float(a[1])
    b1, b2 = float(b[0]), float(b[1])
    arr1 = [[round(a1 + 0.1 * n, 1), round(a2 + 0.1 * m, 1)] for n in range(101) for m in range(101)]
    arr2 = [[round(b1 + 0.1 * n, 1), round(b2 + 0.1 * m, 1)] for n in range(101) for m in range(101)]



    return arr

