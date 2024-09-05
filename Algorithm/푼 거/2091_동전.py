# 목표 금액, 1, 5, 10, 25
X, *coins = list(map(int, input().split()))
# 사용한 동전 종류
dp = [[0, 0, 0, 0] for _ in range(X+1)]
# 사용한 동전 갯수
dp_cnt = [-1] * (X+1)
dp_cnt[0] = 0

for i in range(4):
    having = coins[i]
    value = [1, 5, 10, 25][i]

    if having:
        for j in range(X+1-value):
            if dp_cnt[j] != -1:
                # 지금 동전을 추가하는 게 동전을 더 많이 쓰는 거고
                if dp_cnt[j] + 1 >= dp_cnt[j+value]:
                    # 동전을 더 쓸 수 있다면
                    if dp[j][i] < having:
                        dp[j+value] = [*dp[j]]
                        dp[j+value][i] += 1
                        dp_cnt[j+value] = dp_cnt[j] + 1

print(*dp[-1])
