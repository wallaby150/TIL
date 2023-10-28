import sys, re
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
dots = sorted(list(map(int, input().split())))

def big_dot(num):
    left = 0
    right = N - 1

    while left <= right:
        mid = (left + right) // 2
        if num < dots[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return right

def small_dot(num):
    left = 0
    right = N - 1

    while left <= right:
        mid = (left + right) // 2
        if dots[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return right + 1

for _ in range(M):
    start, end = map(int, input().split())
    print(big_dot(end) - small_dot(start) + 1)
