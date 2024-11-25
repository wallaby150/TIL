X, Y, p1, p2 = map(int, input().split())
cnt = 0

while cnt < 1000:
    if p1 == p2:
        print(p1)
        break
    elif p1 > p2:
        p2 += Y
    else:
        p1 += X
    cnt += 1
else:
    print(-1)