import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())

def bs(li, n):
    s, e = 0, len(li) - 1

    while s <= e:
        m = (s+e) // 2
        if li[m] == n:
            return 1
        elif li[m] < n:
            s = m + 1
        else:
            e = m - 1
    return 0

for _ in range(T):
    N = int(input())
    nums1 = sorted(list(map(int, input().split())))
    M = int(input())
    nums2 = list(map(int, input().split()))

    for num in nums2:
        print(bs(nums1, num))