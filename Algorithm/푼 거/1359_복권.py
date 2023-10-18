import sys
from itertools import combinations
input = lambda : sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
comb = list(combinations(range(N), M))
total_count = 0
hit_count = 0

for c1 in comb:
    for c2 in comb:
        total_count += 1
        tmp = 0

        for num in c1:
            if num in c2:
                tmp += 1

        if tmp >= K:
            hit_count += 1


print(hit_count / total_count)