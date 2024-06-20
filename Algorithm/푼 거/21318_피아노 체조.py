import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
nums = list(map(int, input().split()))
sums = [0]

for i in range(len(nums) - 1):
    if nums[i+1] < nums[i]:
        sums.append(sums[-1] + 1)
    else:
        sums.append(sums[-1])

Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    print(sums[y-1] - sums[x-1])
