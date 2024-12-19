import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
for _ in range(N):
    text = list(input().split(' '))
    print(' '.join(text[2:] + text[:2]))