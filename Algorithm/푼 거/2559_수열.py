import sys

input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
nums = list(map(int, input().split()))

tmp = sum(nums[:K])
answer = tmp

for idx in range(K, N):
    tmp += nums[idx] - nums[idx-K]
    answer = max(tmp, answer)

print(answer)

