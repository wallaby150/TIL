A = int(input())
T = int(input())
S = int(input())

x = y = 0
cnt = 0
tmp = []

while True:
    cnt += 1

    for _ in range(2):
        x += 1
        tmp.append((x, 0))
        y += 1
        tmp.append((y, 1))
    for _ in range(cnt + 1):
        x += 1
        tmp.append((x, 0))
    for _ in range(cnt + 1):
        y += 1
        tmp.append((y, 1))

    if x >= T:
        print(tmp.index((T, S)) % A)
        break
