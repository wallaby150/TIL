import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    P, M = map(int, input().split())
    seats = [False] * (M + 1)

    for _ in range(P):
        num = int(input())
        seats[num] = True

    print(P - seats.count(True))