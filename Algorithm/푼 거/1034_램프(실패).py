import sys
input = lambda : sys.stdin.readline().rstrip()
from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())
table = [list(map(int, input())) for _ in range(N)]
K = int(input())
ans = 0

c = K
if K > M:
    if K % 2 != M % 2:
        c = M - 1
    else:
        c = K

for i in range(c, -1, -2):
    for com in combinations(range(M), i):
        tmp = deepcopy(table)
        cnt = 0
        for x in com:
            for y in range(N):
                tmp[y][x] = 1 if tmp[y][x] == 0 else 0

        for line in tmp:
            if 0 not in line:
                cnt += 1

        ans = max(cnt, ans)

print(ans)

