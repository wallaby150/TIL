import sys
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
nums = list(int(input()) for _ in range(N))

l, r = 1, max(nums)
ans = 0

while l <= r:
    mid = (l + r) // 2
    tmp = sum(num // mid for num in nums)
    if tmp >= K:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)
