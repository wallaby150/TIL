import sys
from itertools import combinations
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
ans = []

for i in range(1, 11):
    for comb in combinations(range(0, 10), i):
        comb = sorted(list(comb), reverse=True)
        ans.append(int("".join(map(str, comb))))

    if len(ans) > N:
        break

ans.sort()

try:
    print(ans[N])
except:
    print(-1)