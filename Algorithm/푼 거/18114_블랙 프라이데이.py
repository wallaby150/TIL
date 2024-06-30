import sys
input = lambda: sys.stdin.readline().rstrip()

N, C = map(int, input().split())
nums = sorted(list(map(int, input().split())))


def binary_search(arr, t):
    l, r = 0, len(arr) - 1

    while l <= r:
        m = (l + r) // 2

        if arr[m] == t:
            return 1
        elif arr[m] > t:
            r = m - 1
        else:
            l = m + 1
    return 0


def solve():
    if binary_search(nums, C):
        return 1

    i, j = 0, N - 1
    while i < j:
        tmp = nums[i] + nums[j]
        if tmp == C:
            return 1

        elif tmp > C:
            j -= 1

        else:
            need = C - tmp
            if nums[i] != need and nums[j] != need and binary_search(nums, need):
                return 1

            i += 1
    return 0


print(solve())
