import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]

for h in range(1, N):
    nums[h][0] += nums[h-1][0]
    for idx in range(1, h):
        nums[h][idx] += max(nums[h-1][idx-1], nums[h-1][idx])
    nums[h][h] += nums[h-1][h-1]

print(max(nums[-1]))