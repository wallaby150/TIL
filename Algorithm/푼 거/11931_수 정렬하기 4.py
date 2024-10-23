import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
nums = sorted([int(input()) for _ in range(N)], reverse=True)

for num in nums:
    print(num)