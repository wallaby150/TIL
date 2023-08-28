import sys
from collections import deque
sys.stdin = open('2667_단지번호붙이기.txt')
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
maps = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
answer = []


def search(y, x):
    q = deque([(x, y)])
    count = 1
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    visited[y][x] = 1

    while q:
        now_x, now_y = q.popleft()
        # visited[now_y][now_x] = 1
        for i in range(4):
            togo_x, togo_y = now_x+dx[i], now_y+dy[i]
            if 0 <= togo_x < N and 0 <= togo_y < N:
                if maps[togo_y][togo_x] == 1 and visited[togo_y][togo_x] == 0:
                    count += 1
                    visited[togo_y][togo_x] = 1
                    q.append((togo_x, togo_y))

    return count


for y in range(N):
    for x in range(N):
        if maps[y][x] == 1:
            if visited[y][x] == 0:
                answer.append(search(y, x))

print(len(answer))
for i in sorted(answer):
    print(i)




'''
3
7
8
9
'''