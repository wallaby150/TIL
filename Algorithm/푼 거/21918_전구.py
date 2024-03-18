N, M = map(int, input().split())
bulbs = [0] + list(map(int, input().split()))
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        bulbs[b] = c
    elif a == 2:
        for i in range(b, c+1):
            bulbs[i] = not bulbs[i]
    elif a == 3:
        for i in range(b, c+1):
            bulbs[i] = 0
    else:
        for i in range(b, c+1):
            bulbs[i] = 1

for j in range(1, N+1):
    if bulbs[j]:
        print(1, end=' ')
    else:
        print(0, end=' ')