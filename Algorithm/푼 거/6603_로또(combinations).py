import sys
from itertools import combinations
input = lambda : sys.stdin.readline().rstrip()


while True:
    tmp = list(map(int, input().split()))
    if tmp == [0]:
        break

    K, S = tmp[0], tmp[1:]
    for com in combinations(S, 6):
        print(*com)
    print()