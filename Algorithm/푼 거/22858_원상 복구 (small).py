import sys
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
ans = list(map(int, input().split()))
D = list(map(int, input().split()))

for _ in range(K):
    tmp = [0]*N
    for i in range(N):
        tmp[D[i]-1] = ans[i]
    ans = tmp
print(*ans)