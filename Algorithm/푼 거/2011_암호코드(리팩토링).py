code = input()

if code[0] == '0':
    print(0)
    exit()

dp = [0] * (len(code) + 1)
dp[0], dp[1] = 1, 1

for i in range(2, len(code) + 1):
    if code[i - 1] > '0':
        dp[i] += dp[i - 1]

    two_digits = int(code[i - 2:i])
    if 10 <= two_digits <= 26:
        dp[i] += dp[i - 2]

print(dp[-1] % 1000000)
