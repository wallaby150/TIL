N, S = map(int, input().split())

if S <= 1:
    print(1)
    exit()

nums = list(map(int, input().split()))

ans = 200000
l, r = 0, 0
tmp = 0

while r < N:
    r += 1
    tmp += nums[r - 1]

    while tmp >= S:
        ans = min(ans, r - l)
        tmp -= nums[l]
        l += 1

print(ans if ans != 200000 else 0)
