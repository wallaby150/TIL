import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
nums = sorted(list(map(int, input().split())))
ans = 0
l, r = 0, N-1

while l < r:
    small, big = nums[l], nums[r]
    if small + big == M:
        ans += 1
        r -= 1
        l += 1
    elif small + big > M:
        r -= 1
    else:
        l += 1

print(ans)