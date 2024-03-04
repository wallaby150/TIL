T = int(input())
for _ in range(T):
    J, N = map(int, input().split())
    boxes = []

    for _ in range(N):
        a, b = map(int, input().split())
        boxes.append(a * b)
    boxes.sort(reverse=True)

    ans, tmp = 0, 0
    for box in boxes:
        tmp += box
        ans += 1
        if tmp >= J:
            break

    print(ans)