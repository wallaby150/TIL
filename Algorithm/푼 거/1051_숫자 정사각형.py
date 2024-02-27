import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = []

for i in range(N):
    arr.append(list(input()))

c = min(N, M)
answer = 0
for i in range(N):
    for j in range(M):
        for k in range(c):
            if ((i + k) < N) and ((j + k) < M) and (arr[i][j] == arr[i][j + k] == arr[i + k][j] == arr[i + k][j + k]):
                answer = max(answer, (k + 1) ** 2)

print(answer)