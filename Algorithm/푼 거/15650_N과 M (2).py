from itertools import combinations

N, M = map(int, input().split())
for a in combinations(range(1, N+1), M):
    print(*a)