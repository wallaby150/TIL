N, M = map(int, input().split())
bad = [[] for num in range(N)]
count = 0

for _ in range(M):
    a, b = map(int, input().split())
    bad[a-1].append(b-1)
    bad[b-1].append(a-1)

for i in range(N):
    for j in range(N):
        if i == j:
            continue

        elif j in bad[i]:
            continue

        for k in range(N):
            if i == k:
                continue

            elif k in bad[i]:
                continue

            count += 1

print(count)
