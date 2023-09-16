import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N = int(input())
    nums1 = set(list(map(int, input().split())))
    M = int(input())
    nums2 = list(map(int, input().split()))

    for num in nums2:
        if num in nums1:
            print(1)
        else:
            print(0)