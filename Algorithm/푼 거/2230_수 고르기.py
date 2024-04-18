import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = [int(input()) for _ in range(N)]
nums.sort()
l, r = 0, 0
ans = nums[-1] - nums[0]

while r < N:
    tmp = nums[r] - nums[l]

    if tmp < M:
        r += 1

    elif tmp == M:
        ans = tmp
        break

    else:
        l += 1
        ans = min(ans, tmp)

print(ans)
