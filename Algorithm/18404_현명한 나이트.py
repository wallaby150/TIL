import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

# 체스판 크기, 상대 말의 갯수
N, M = map(int, input().split())
# 나이트의 위치 y, x
ky, kx = list(map(int, input().split()))

# 체스판
board = [[10000001] * N for _ in range(N)]
board[ky-1][kx-1] = 0

# 적들의 위치
enemys = []
for _ in range(M):
    y, x = map(int, input().split())
    enemys.append([x-1, y-1])
    board[y-1][x-1] = -1

# 잡은 말 갯수
count = 0

move_x = [-2, -2, -1, -1, 1, 1, 2, 2]
move_y = [-1, 1, -2, 2, -2, 2, -1, 1]

q = deque([])
q.append([ky-1, kx-1])

while q:
    now_y, now_x = q.popleft()
    for i in range(8):
        togo_y, togo_x = now_y + move_y[i], now_x + move_x[i]
        if 0 <= togo_y < N and 0 <= togo_x < N:
            # 병정이 있는 자리면
            if board[togo_y][togo_x] == -1:
                count += 1
                board[togo_y][togo_x] = board[now_y][now_x] + 1
                q.append([togo_y, togo_x])

                # 병정 다 체크했으면 끝
                if count == M:
                    q = []
                    break

            # 없는 자리면
            else:
                if board[togo_y][togo_x] > board[now_y][now_x] + 1:
                    board[togo_y][togo_x] = board[now_y][now_x] + 1
                    q.append([togo_y, togo_x])

for e in enemys:
    print(board[e[1]][e[0]], end=' ')
