H, W = map(int, input().split())
hs = list(map(int, input().split()))

if W < 3:
    print(0)

else:
    ans = 0

    for i in range(1, W-1):
        left = max(hs[:i])
        right = max(hs[i+1:])

        low = min(left, right)
        if low > hs[i]:
            ans += low - hs[i]

    print(ans)
