import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 10000000
visited = [False] * N

def dfs(idx, depth):
    global ans

    if depth == N//2:
        s = 0
        l = 0

        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    s += graph[i][j]

                elif not visited[i] and not visited[j]:
                    l += graph[i][j]

        ans = min(ans, abs(s - l))
        return


    for i in range(idx, N):
        if visited[i] == False:
            visited[i] = True
            dfs(i + 1, depth + 1)
            visited[i] = False

dfs(0, 0)
print(ans)