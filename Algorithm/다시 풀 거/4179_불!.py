import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque



# 미로의 행과 열
R, C = map(int, input().split())
miro = list(list(map(str, input())) for _ in range(R))

#
J_start = deque()
F_start = deque()

temp_F = []
for y in range(R):
    for x in range(C):
        if miro[y][x] == 'J':
           J_start.append([[y, x]])
           miro[y][x] = 0
        elif miro[y][x] == 'F':
           temp_F.append([y, x])
else:
    F_start.append(temp_F)

def solve(J_queue, F_queue, R, C):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    f_miro = list([0] * C for _ in range(R))

    while J_queue != deque([]):
        now_J = J_queue.popleft()
        if F_queue != deque([]):
            now_F = F_queue.popleft()

        temp = []
        # 지훈이가 움직임
        while now_J:
            J = now_J.pop()
            now_y, now_x = J[0], J[1]

            # 여기 불이 번졌으면 통과해야 함.
            if f_miro[now_y][now_x]:
                continue

            for dir in range(4):
                togo_y, togo_x = now_y + dy[dir], now_x + dx[dir]

                # 벽을 통과했으면 움직임.
                if togo_y == -1 or togo_y == R:
                    return miro[now_y][now_x] + 1
                if togo_x == -1 or togo_x == C:
                    return miro[now_y][now_x] + 1

                if miro[togo_y][togo_x] == '.':
                    miro[togo_y][togo_x] = miro[now_y][now_x] + 1
                    temp.append([togo_y, togo_x])
        if temp != []:
            J_queue.append(temp)


        temp = []
        # 불이 움직임
        while now_F:
            F = now_F.pop()
            now_fy, now_fx = F[0], F[1]
            f_miro[now_fy][now_fx] = 1

            for dir in range(4):
                togo_fy, togo_fx = now_fy + dy[dir], now_fx + dx[dir]

                if 0 <= togo_fy < R and 0 <= togo_fx < C:
                    # 벽이 아니라면 불이 번진다.
                    if miro[togo_fy][togo_fx] != '#' and f_miro[togo_fy][togo_fx] == 0:
                        temp.append([togo_fy, togo_fx])
                        f_miro[togo_fy][togo_fx] = 1
        if temp != []:
            F_queue.append(temp)

    return 'IMPOSSIBLE'

print(solve(J_start, F_start, R, C))

