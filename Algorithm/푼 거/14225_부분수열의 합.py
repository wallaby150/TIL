import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
S = list(map(int, input().split()))
answer = set(S)

for i in range(2, len(S)+1):
    for com in combinations(S, i):
        answer.add(sum(com))

for num in range(1, 100000000001):
    if num not in answer:
        print(num)
        break
