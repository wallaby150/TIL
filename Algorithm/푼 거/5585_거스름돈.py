ㅉN = 1000 - int(input())
ans = 0

for c in [500, 100, 50, 10, 5, 1]:
    if N == 0:
        break

    if N // c:
        ans += N // c
        N %= c

print(ans)