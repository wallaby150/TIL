import sys
from collections import Counter
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
participants = list(input() for _ in range(N))
counts = Counter(participants)
for _ in range(N-1):
    name = input()
    counts[name] -= 1

print(counts.most_common(1)[0][0])