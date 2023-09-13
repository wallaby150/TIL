import sys
from itertools import permutations
input = lambda : sys.stdin.readline().rstrip()

# 재귀함수로 다시 풀어보기

N = int(input())
K = int(input())
cards = list(input() for _ in range(N))
ans = set()

for p in permutations(cards, K):
    tmp = ''
    for i in range(K):
        tmp += p[i]
    ans.add(tmp)


print(len(ans))