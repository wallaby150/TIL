import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())
for i in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    print(min(nums), max(nums))