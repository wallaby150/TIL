import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(N)]

K = int(input())
for _ in range(K):
    j, i, y, x = map(int, input().split())
    ans = 0
    for b in range(j-1, y):
        for a in range(i-1, x):
            ans += nums[b][a]
    print(ans)
