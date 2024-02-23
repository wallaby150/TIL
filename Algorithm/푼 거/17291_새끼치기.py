N = int(input())
dp = [1, 2, 4, 7]

while N > len(dp):
    # 홀수년 차례면
    if len(dp) % 2 == 0:
        dp.append(dp[-1] * 2)
    else:
        dp.append(dp[-1] * 2 - dp[-4] - dp[-5])

print(dp[N-1])