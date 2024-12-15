for _ in range(int(input())):
    N, A, B = map(int, input().split())
    T = bin(min(A, B))[::-1].index('1')
    print(N - T)
