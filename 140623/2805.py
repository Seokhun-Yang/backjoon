import sys

numOfTree, lenOfTree = map(int, sys.stdin.readline().rstrip().split())
trees = list(map(int, sys.stdin.readline().rstrip().split()))


def search(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if target == mid:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return 0


print(search(trees, 0, max(trees), lenOfTree))
