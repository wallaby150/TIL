N, M = map(int, input().split())
nums = list(map(int, input().split()))

l, r = 0, (M // N + 1) * max(nums)
ans = 0

while l <= r:
    m = (l + r) // 2
    cnt = 0
    for num in nums:
        cnt += m // num
        if cnt >= M:
            break

    if cnt >= M:
        ans = m
        r = m - 1
    else:
        l = m + 1

print(ans)
