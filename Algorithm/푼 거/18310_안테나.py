import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
nums = sorted(list(map(int, input().split())))
print(nums[(N-1) // 2])