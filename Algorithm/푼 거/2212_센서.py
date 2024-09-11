import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
K = int(input())
nums = list(map(int, input().split()))

if N <= K:
    print(0)
else:
    nums.sort()
    dist = sorted([nums[i+1] - nums[i] for i in range(N-1)])
    print(sum(dist[:N-K]))