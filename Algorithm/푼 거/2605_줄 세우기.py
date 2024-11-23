import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
nums = list(map(int, input().split()))
ans = []

for i in range(N):
    ans.insert(i - nums[i], i + 1)

print(' '.join(map(str, ans)))
