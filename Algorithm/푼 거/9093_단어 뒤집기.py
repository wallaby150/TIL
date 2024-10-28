import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    for word in input().split(' '):
        print(word[::-1], end=' ')
    print()