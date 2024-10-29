import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
tmp = set()

for _ in range(T):
    now = input()
    tmp.add(now[::-1])
    if now in tmp:
        print(len(now), now[len(now)//2])
        break