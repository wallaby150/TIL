import sys
input = lambda: sys.stdin.readline().rstrip()

N, M, R = map(int, input().split())
visited = [0] * (N + 1)
tmp = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    tmp[u].append(v)
    tmp[v].append(u)

connect = [sorted(tmp[i], reverse=True) for i in range(N+1)]

stack = [R]
cnt = 0

while stack:
    now = stack.pop()
    if visited[now] != 0:
        continue

    cnt += 1
    visited[now] = cnt

    for togo in connect[now]:
        if visited[togo] == 0:
            stack.append(togo)

print("\n".join(map(str, visited[1:])))
