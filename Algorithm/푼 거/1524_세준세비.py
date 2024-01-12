import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())
for i in range(T):
    input()
    N, M = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse = True)
    b = sorted(list(map(int, input().split())), reverse = True)

    while a and b:
        if a[-1] >= b[-1]:
            b.pop()
        else:
            a.pop()

    if a:
        print('S')
    elif b:
        print('B')
    else:
        print('C')