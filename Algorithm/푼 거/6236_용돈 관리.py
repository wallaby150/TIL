import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = list(int(input()) for _ in range(N))
l, r = max(nums), sum(nums)

while l <= r:
    m = (l + r) // 2
    now = m
    draw = 1

    for num in nums:
        if now >= num:
            now -= num
        else:
            draw += 1
            now = m - num

    if draw > M:
        l = m + 1
    else:
        r = m - 1

print(m)