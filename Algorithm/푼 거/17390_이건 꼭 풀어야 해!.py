import sys
input = lambda: sys.stdin.readline().rstrip()

N, Q = map(int, input().split())
nums = sorted(list(map(int, input().split())))
for i in range(1, N):
    nums[i] += nums[i-1]
nums = [0] + nums

for _ in range(Q):
    L, R = map(int, input().split())
    print(nums[R] - nums[L-1])
