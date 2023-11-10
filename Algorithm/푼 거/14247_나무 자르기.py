import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
H = list(map(int, input().split()))
A = list(map(int, input().split()))

cut = sorted(list(zip(H, A)), key=lambda x: x[1])
answer = sum(H)
for i in range(N):
    answer += cut[i][0] + cut[i][1] * i

print(answer)