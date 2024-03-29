import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
table = [list(map(int, input())) for _ in range(N)]
K = int(input())
ans = 0



# 어디 인덱스를 확인하고 있는지, 가능한 수가 뭐가 남았는지, 몇 번 바꿨는지
def solve(idx, p, cnt):
    global ans

    if idx == M:
        if cnt in range(K, -1, -2):
            ans = max(ans, len(p))
        return


    on = []
    off = []
    # 여태 가능한 숫자 중에서
    for i in p:
        if table[i][idx]:
            on.append(i)
        else:
            off.append(i)

    if cnt < K:
        if len(off):
            solve(idx + 1, off, cnt + 1)
    if len(on):
        solve(idx + 1, on, cnt)
    return


solve(0, list(range(N)), 0)
print(ans)