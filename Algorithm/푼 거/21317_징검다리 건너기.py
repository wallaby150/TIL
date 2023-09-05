import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
cost_list = list(list(map(int, input().split())) for _ in range(N-1))
k = int(input())

# 매우 큰 점프 사용 O, 사용 x
ans = [[100001, 100001] for _ in range(25)]
ans[0] = [0, 0]

for i in range(N-1):
    # 매우 큰 점프 사용 여부에 따라
    for j in range(2):
        ans[i+1][j] = min(ans[i+1][j], ans[i][j] + cost_list[i][0])
        ans[i+2][j] = min(ans[i+2][j], ans[i][j] + cost_list[i][1])

        if j == 1:
            ans[i + 3][0] = min(ans[i + 3][0], ans[i][1] + k)

print(min(ans[N-1]))