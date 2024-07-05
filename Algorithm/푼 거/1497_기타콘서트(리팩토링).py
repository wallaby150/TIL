import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
guitars = set()
ans, use = 0, 100

for _ in range(N):
    g, p = input().split()
    p = p.replace('Y', '1')
    p = p.replace('N', '0')
    guitars.add(int(p, 2))

guitars -= {0}
if not guitars:
    print(-1)
    exit()

for i in range(1, len(guitars) + 1):
    for comb in combinations(guitars, i):
        now = 0
        for case in comb:
            now = now | case

        play = 0
        for j in range(M):
            if now & (1 << j):
                play += 1
        if play > ans:
            ans = play
            use = i

print(use)
