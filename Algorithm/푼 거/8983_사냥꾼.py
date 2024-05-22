import sys
input = lambda : sys.stdin.readline().rstrip()

M, N, L = map(int, input().split())
nums = sorted(list(map(int, input().split())))
cnt = 0

for _ in range(N):
    x, y = map(int, input().split())

    l, r = 0, M-1

    while l <= r:
        mid = (l + r) // 2
        now_m = nums[mid]
        if abs(now_m - x) + y <= L:
            cnt += 1
            break

        if now_m == x:
            break
        elif now_m > x:
            r = mid - 1
        else:
            l = mid + 1

print(cnt)
