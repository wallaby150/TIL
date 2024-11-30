import sys
from collections import Counter
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
for _ in range(N):
    a, b = input().split()
    if Counter(a) == Counter(b):
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')
