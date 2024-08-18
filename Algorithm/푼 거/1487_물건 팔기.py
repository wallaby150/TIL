import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
nums = sorted([list(map(int, input().split())) for _ in range(N)])
ans = high = 0

for i in range(N):
    price = nums[i][0]
    benefit = 0

    for j in range(i, N):
        benefit += max(0, price - nums[j][1])

    if high < benefit:
        high = benefit
        ans = price

print(ans)
