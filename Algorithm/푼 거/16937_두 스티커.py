import sys
input = lambda: sys.stdin.readline().rstrip()

H, W = map(int, input().split())
N = int(input())
stickers = []
ans = 0

for _ in range(N):
    stickers.append(tuple(map(int, input().split())))

for i in range(N):
    for j in range(i + 1, N):
        for r1, c1 in stickers[i], (stickers[i][1], stickers[i][0]):  # 회전 고려
            for r2, c2 in stickers[j], (stickers[j][1], stickers[j][0]):  # 회전 고려
                # 겹침 조건 수정 (x 좌표 범위 또는 y 좌표 범위가 겹치지 않아야 함)
                if (r1 + r2 <= H and max(c1, c2) <= W) or (c1 + c2 <= W and max(r1, r2) <= H):
                    ans = max(ans, r1 * c1 + r2 * c2)

print(ans)
