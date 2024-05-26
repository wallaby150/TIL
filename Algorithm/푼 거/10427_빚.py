import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    tmp = list(map(int, input().split()))
    N, nums = tmp[0], sorted(tmp[1:])
    # 누적합 cs
    cs, s = [0] * (N + 1), 0
    for i in range(N):
        s += nums[i]
        cs[i+1] = s

    ans = 0
    for j in range(2, N+1):
        low = float('inf')
        for k in range(N-j+1):
            now = nums[k+j-1] * j - (cs[k+j] - cs[k])
            low = min(low, now)

        ans += low
    print(ans)
