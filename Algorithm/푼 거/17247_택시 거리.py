import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

point1, point2 = None, None

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 1:
            if not point1:
                point1 = (i, j)
            else:
                point2 = (i, j)

ans = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

print(ans)
