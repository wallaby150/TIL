N = int(input())

if N % 2:
    h = N // 2
    print('*' * N)
    print(' ' * (N - h - 1) + '*')
    for i in range(h):
        print(' ' * (h - i - 1) + '*' + ' ' * (2 * i + 1) + '*')
else:
    print("I LOVE CBNU")
