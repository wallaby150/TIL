import sys
from collections import defaultdict
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
q = defaultdict(int)

for _ in range(N):
    name, extension = input().split('.')
    q[extension] += 1

for ex in sorted(q.items()):
    print(*ex)