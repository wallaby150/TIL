H, W = map(int, input().split())
hs = list(map(int, input().split()))
ans = 0

if W < 3:
    print(0)

else:
    for y in range(1, H+1):
        left = False
        tmp = 0
        for x in range(W):
            # 왼쪽이 생김
            if not left and hs[x] >= y:
                left = True
            # 왼쪽이 있고 비었으면
            elif left and hs[x] < y:
                tmp += 1
            # 왼쪽이 있고 오른쪽
            elif left and hs[x] >= y:
                ans += tmp
                tmp = 0

    print(ans)
