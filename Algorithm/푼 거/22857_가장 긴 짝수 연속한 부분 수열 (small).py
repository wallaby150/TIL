import sys
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
S = list(map(int, input().split()))

left = 0
right = 0
ans = 0
cnt = 0

while right < N:
    # 홀수 갯수가 K개를 넘었으면
    if cnt > K:
        # 홀수라면
        if S[left] % 2:
            cnt -= 1
        left += 1

    else:
        # 홀수라면
        if S[right] % 2:
            cnt += 1
        right += 1

    if cnt <= K:
        ans = max(ans, right - left - cnt)

print(ans)
