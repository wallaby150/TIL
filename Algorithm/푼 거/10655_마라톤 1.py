import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
check = list(list(map(int, input().split())) for _ in range(N))
dist = []
jump = []

for i in range(N-1):
    tmp = abs(check[i][0] - check[i+1][0]) + abs(check[i][1] - check[i+1][1])
    dist.append(tmp)

    if i != N - 2:
        tmp2 = abs(check[i][0] - check[i+2][0]) + abs(check[i][1] - check[i+2][1])
        jump.append(tmp2)

diff = 0
for j in range(N-2):
    diff = max(diff, dist[j] + dist[j+1] - jump[j])

print(sum(dist) - diff)
