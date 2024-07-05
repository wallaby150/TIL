import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
guitars = set()
ans, use = 0, 100

target = int('1' * M, 2)
for _ in range(N):
    g, p = input().split()
    p = p.replace('Y', '1')
    p = p.replace('N', '0')
    p = int(p, 2)
    if p == target:
        print(1)
        exit()
    if p != 0:
        guitars.add(p)

l = len(guitars)
for i in range(1, l+1):
    for comb in combinations(guitars, i):
        now = 0
        for case in comb:
            now = now | case

        play = bin(now).count('1')
        if play > ans:
            ans = play
            use = i

if ans == 0:
    print(-1)
else:
    print(use)
