import sys
input = lambda: sys.stdin.readline().rstrip()

dp = ['-', '- -', '- -   - -', '- -   - -         - -   - -']


def recur(n):
    if n <= 3:
        return dp[n]
    else:
        low = recur(n-1)
        return low + ' ' * 3 ** (n-1) + low


while True:
    try:
        N = int(input())
        print(recur(N))
    except:
        break
