import sys
input = lambda: sys.stdin.readline().rstrip()

N = list(map(int, input()))
L = len(N)

if L == 1:
    print('NO')
else:
    a = b = 1
    for i in range(L - 1):
        a = b = 1
        for j in range(i + 1):
            a *= N[j]
        for k in range(i + 1, L):
            b *= N[k]
        if a == b:
            break

    if a == b:
        print('YES')
    else:
        print('NO')