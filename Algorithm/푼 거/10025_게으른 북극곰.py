import sys
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
ground = [0] * 1000001
last = 0

for _ in range(N):
    i, g = map(int, input().split())
    ground[g] = i
    last = max(last, g)

window = sum(ground[:2*K + 1]) # 초기 윈도우 합
ans = window
s = 2*K+1

for i in range(s, last + 1):
    window -= ground[i-s] # 윈도우의 맨 앞 값 빼기
    window += ground[i] # 윈도우의 맨 뒤 값 더하기
    ans = max(ans, window) # 최댓값 갱신

print(ans)
