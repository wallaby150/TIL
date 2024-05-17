import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = sorted([int(input()) for _ in range(N)])

def search(num):
    l, r = 0, N - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] > num:
            r = mid - 1
        elif nums[mid] < num:
            l = mid + 1
        else:
            if r == mid:
                break
            r = mid

    if nums[mid] == num:
        return mid
    else:
        return -1


for _ in range(M):
    t = int(input())
    print(search(t))

