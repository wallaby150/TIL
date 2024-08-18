import sys
input = lambda: sys.stdin.readline().rstrip()

H, W, X, Y = map(int, input().split())

ans = []
graph = [list(map(int, input().split())) for _ in range(H + X)]

for i in range(H):
    ans.append(graph[i][:W])

for j in range(H):
    for k in range(W):
        if j + X < H and k + Y < W:
            ans[j + X][k + Y] -= ans[j][k]

for line in ans:
    print(*line)
