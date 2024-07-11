import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = [[0] * (M + 1)]

for i in range(N):
    tmp = [0] + list(map(int, input().split()))

    for j in range(1, M+1):
        tmp[j] += tmp[j-1] + nums[i][j] - nums[i][j-1]
    nums.append(tmp)

K = int(input())
for _ in range(K):
    j, i, y, x = map(int, input().split())
    ans = nums[y][x] - nums[j-1][x] - nums[y][i-1] + nums[j-1][i-1]
    print(ans)
