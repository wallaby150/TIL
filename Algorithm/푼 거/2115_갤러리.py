import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
grid = list(input() for _ in range(N))
# 상, 하, 좌, 우의 벽을 썼는지 확인
visited = [[[0, 0, 0, 0] for _ in range(M)] for _ in range(N)]
ans = 0

for y in range(1, N - 1):
    for x in range(1, M - 1):
        # 지금 칸이 빈칸일 때
        if grid[y][x] == '.':
            # 오른쪽이 비어있다면
            if grid[y][x + 1] == '.':
                # 위쪽 벽이 있고, 그걸 안 썼다면
                if grid[y - 1][x] == 'X' and not visited[y][x][0]:
                    # 오른쪽 칸의 윗쪽에 벽이 있는지 확인
                    if grid[y-1][x+1] == 'X':
                        ans += 1
                        # 오른쪽 칸의 윗쪽 벽은 사용
                        visited[y][x+1][0] = 1
                # 아래쪽 벽이 있고, 그걸 안 썼다면
                if grid[y+1][x] == 'X' and not visited[y][x][1]:
                    # 오른쪽 칸의 아랫쪽 벽이 있는지 확인
                    if grid[y+1][x+1] == 'X':
                        ans += 1
                        visited[y][x+1][1] = 1

            # 아래쪽이 비어있다면
            if grid[y+1][x] == '.':
                if grid[y][x-1] == 'X' and not visited[y][x][2]:
                    if grid[y+1][x-1] == 'X':
                        ans += 1
                        visited[y+1][x][2] = 1
                if grid[y][x+1] == 'X' and not visited[y][x][3]:
                    if grid[y+1][x+1] == 'X':
                        ans += 1
                        visited[y+1][x][3] = 1

print(ans)