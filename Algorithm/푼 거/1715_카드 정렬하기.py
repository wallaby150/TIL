import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
grid = list(input() for _ in range(N))
visited = [[False] * M for _ in range(N)]
ans = 0

def DFS(y, x, now):
    global ans

    # 빈 칸 리스트를 저장할 스택
    stack = []
    tmp = now[:]

    # 상하좌우에 벽/빈 칸이 있는지 확인
    for i in range(4):
        ty, tx = y + [-1, 0, 1, 0][i], x + [0, 1, 0, -1][i]
        if grid[ty][tx] == '.':
            tmp[i] = 0
            if not visited[ty][tx]:
                stack.append((ty, tx))
                visited[ty][tx] = True
        else:
            tmp[i] += 1
            if tmp[i] == 2:
                print(y, x, '상우하좌'[i])
                ans += 1
                tmp[i] = 0

    # 스택에 담아둔 곳으로 이동
    while stack:
        yy, xx = stack.pop()
        DFS(yy, xx, tmp)

    return


for Y in range(1, N - 1):
    for X in range(1, M - 1):
        if grid[Y][X] == '.' and not visited[Y][X]:
            visited[Y][X] = True
            DFS(Y, X, [0, 0, 0, 0])

print(ans)