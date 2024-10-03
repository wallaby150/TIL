import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
visited = [[False] * N for _ in range(N)]
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0),
              (1, -1), (0, -1), (-1, -1)]


def dfs(y, x, cnt):
    if x == N:
        y += 1
        x = 0

    if y == N:
        return 0


    now = 0

    if not visited[y][x]:
        if cnt == N - 1:
            now += 1
        else:
            # 모든 방면의 이동경로를 차단
            tmp = [(y, x)]
            visited[y][x] = True
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                while 0 <= ny < N and 0 <= nx < N:
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        tmp.append((ny, nx))
                    ny += dy
                    nx += dx
            # 다음 경로 가보기
            now += dfs(y, x + 1, cnt + 1)
            while tmp:
                by, bx = tmp.pop()
                visited[by][bx] = False
    now += dfs(y, x + 1, cnt)
    return now


print(dfs(0, 0, 0))
