import sys
input = lambda : sys.stdin.readline().rstrip()

while True:
    N = int(input())
    if N == 0:
        break
    names = sorted([input() for _ in range(N)], key=str.lower)
    print(names[0])