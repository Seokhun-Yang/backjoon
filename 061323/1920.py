import sys

n1 = int(sys.stdin.readline().rstrip())
list1 = list(map(int, sys.stdin.readline().rstrip().split()))
n2 = int(sys.stdin.readline().rstrip())
list2 = list(map(int, sys.stdin.readline().rstrip().split()))

list1.sort()


def search(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if target == arr[mid]:
            return 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return 0


for n in list2:
    print(search(list1, 0, len(list1) - 1, n))
