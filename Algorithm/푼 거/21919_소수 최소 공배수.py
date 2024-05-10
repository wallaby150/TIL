import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
nums = set(map(int, input().split()))
ans = 1
l = max(nums)

prime = [True] * (l + 1)

for i in range(2, l + 1):
    for j in range(i * 2, l + 1, i):
        prime[j] = False

for num in nums:
    if prime[num]:
        ans *= num

if ans == 1:
    print(-1)
else:
    print(ans)
