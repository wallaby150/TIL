N, K = map(int, input().split())
A = list(map(int, input().split(',')))

for _ in range(K):
    t = [A[i + 1] - A[i] for i in range(len(A) - 1)]
    A = t

print(*A, sep=',')