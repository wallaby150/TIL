import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
nums = list(map(int, input().split()))

s = [0] * (N + 1)
d = [0] * (N + 1)
for i in range(1, N + 1):
    s[i] = nums[i - 1]
    max_val, min_val = float('-inf'), float('inf')
    for j in range(i, 0, -1):
        max_val = max(max_val, s[j])
        min_val = min(min_val, s[j])
        d[i] = max(d[i], max_val - min_val + d[j - 1])

print(d[-1])