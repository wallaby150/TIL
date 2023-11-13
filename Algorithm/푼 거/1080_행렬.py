import sys
input = lambda: sys.stdin.readline().rstrip()

# 세로 N, 가로 M
N, M = map(int, input().split())
A = list(list(map(int, input())) for _ in range(N))
B = list(list(map(int, input())) for _ in range(N))
answer = 0


def change(sy, sx):
    for dy in range(3):
        for dx in range(3):
            A[sy+dy][sx+dx] = not A[sy+dy][sx+dx]


for y in range(N-2):
    for x in range(M-2):
        if A[y][x] != B[y][x]:
            change(y, x)
            answer += 1

if A != B:
    print(-1)
else:
    print(answer)

