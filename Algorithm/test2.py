import sys
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
nums = list(i for i in range(1, N + 1))
ans = []
num = 0

for j in range(N):
    num += K - 1
    if num >= len(nums):
        num %= len(nums)

    ans.append(nums.pop(num))

print("<", ", ".join(map(str, ans)), ">", sep='')