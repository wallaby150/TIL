A, B, C, X, Y = map(int, input().split())

if A + B < 2 * C:
    print(A * X + B * Y)
else:
    ans = 2 * C * min(X, Y)
    if X >= Y:
        dif = X - Y
        ans += min(A * dif, 2 * C * dif)
    else:
        dif = Y - X
        ans += min(B * dif, 2 * C * dif)
    print(ans)
