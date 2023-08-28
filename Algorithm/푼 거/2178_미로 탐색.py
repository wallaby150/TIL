import sys
from collections import deque
sys.stdin = open("2178_미로 탐색.txt")
input = lambda: sys.stdin.readline().rstrip()


def BFS():
    queue = deque([[0, 0, 1]])

    while queue:
        now_y, now_x, now_count = queue.popleft()
        dx = [0, 0, 1, -1]
        dy = [-1, 1, 0, 0]

        for dir in range(4):
            togo_y, togo_x = now_y + dy[dir], now_x + dx[dir]
            # 갈 수 있는 곳이고
            if 0 <= togo_y < N and 0 <= togo_x < M:
                if maps[togo_y][togo_x] == 1 and visited[togo_y][togo_x] > now_count +1:
                    queue.append([togo_y, togo_x, now_count+1])
                    visited[togo_y][togo_x] = now_count+1


for _ in range(int(input())):
    N, M = map(int, input().split())
    maps = list(list(map(int, input())) for _ in range(N))
    visited = [[N*M+1] * M for _ in range(N)]
    visited[0][0] = 1
    BFS()
    print(visited[N-1][M-1])


'''
15
9
38
13
'''