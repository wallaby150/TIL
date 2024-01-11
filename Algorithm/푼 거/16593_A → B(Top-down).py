import sys
input = lambda: sys.stdin.readline().rstrip()


A, B = map(int, input().split())
count = 0

while A < B:
    if B % 2 == 0:
        B //= 2
    elif B % 10 == 1:
        B //= 10
    else:
        break

    count += 1

if A == B:
    print(count + 1)
else:
    print(-1)