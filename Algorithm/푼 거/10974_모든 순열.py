from itertools import permutations

N = int(input())
for per in permutations(range(1, N+1), N):
    print(*per)