import sys
input = lambda : sys.stdin.readline().rstrip()

na, nb = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

c = list(a - b)
if len(c) == 0:
    print(0)
else:
    print(len(c))
    print(' '.join(map(str, sorted(c))))