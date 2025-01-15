N, M = map(int, input().split())
result = ""
l = len(str(N))
cnt = 0

for _ in range(N):
    result += str(N)
    cnt += l

    if cnt >= M:
        break

print(result[:M])
