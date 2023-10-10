import sys, math
from itertools import combinations
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
H = list(map(int, input().split()))
ans = []

coms = combinations(H, M)
sums = set()
for c in coms:
    sums.add(sum(c))

for num in sums:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            break
    else:
        ans.append(num)

ans.sort()

if not ans:
    print(-1)
else:
    print(*ans)
