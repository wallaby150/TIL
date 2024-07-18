import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
visited = [False] * N
ans = 10 ** 8
grid = list(list(map(int, input().split())) for _ in range(N))


def dfs(start, cnt):
    global ans
    if cnt == N // 2:
        a = b = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    a += grid[i][j]
                elif not visited[i] and not visited[j]:
                    b += grid[i][j]

        ans = min(ans, abs(a - b))
        return

    for k in range(start, N):
        if not visited[k]:
            visited[k] = True
            dfs(k + 1, cnt + 1)
            visited[k] = False
    return


for l in range(N - 1):
    dfs(0, l)

print(ans)
