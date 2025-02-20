N, R, C = map(int, input().split())

for i in range(N):
    for j in range(N):
        if (i + j) % 2 == (R + C) % 2:
            print('v', end='')
        else:
            print('.', end='')
    print()
