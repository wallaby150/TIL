import sys
input = lambda: sys.stdin.readline().rstrip()

N, X = map(int, input().split())
nums = list(map(int, input().split()))
high, cnt = 0, 0

if N == X:
    print(sum(nums))
else:
    l, r = 0, 0
    now = 0
    while r < N:
        r += 1
        now += nums[r-1]

        if r - l > X:
            now -= nums[l]
            l += 1

        if high < now:
            high = now
            cnt = 1
        elif high == now:
            cnt += 1

if high == 0:
    print("SAD")
else:
    print(high)
    print(cnt)