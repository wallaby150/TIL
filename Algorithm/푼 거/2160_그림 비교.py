import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
paints = []
diff = [[36] * N for _ in range(N)]

# 그림들을 입력 받음.
for _ in range(N):
    tmp = []
    for _ in range(5):
        tmp.append(input())
    paints.append(tmp)

# 현재 그림의 인덱스 i
for i in range(N-1):
    # 비교할 그림의 인덱스 j
    for j in range(i+1, N):
        cnt = 0
        for y in range(5):
            for x in range(7):
                if paints[i][y][x] != paints[j][y][x]:
                    cnt += 1
        diff[i][j] = cnt
        diff[j][i] = cnt

low = 36
for k in range(N):
    for l in range(N):
        if diff[k][l] < low:
            low = diff[k][l]
            ans = [k, l]

print(ans[0] + 1, ans[1] + 1)