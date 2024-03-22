T = int(input())

def solve(now, idx, cal, cnt):
    global ans

    # 지금 한 쪽면만 있으면 확인
    if len(now) == 0 or len(now) == 9:
        ans = min(ans, cnt)

    tmp = now[:]
    # 지금이 끄트머리라면 종료
    if idx == 9:
        return

    # 세로로 뒤집기
    if cal == 1:
        for i in range(3):
            tmp[i * 3 + idx % 3] = not tmp[i * 3 + idx % 3]
        solve(tmp, idx, cal + 1, cnt + 1)

    # 가로로 뒤집기
    elif cal == 2:
        pass

    # 대각선 뒤집기
    elif cal == 3:
        if idx in (0, 4, 8):
            pass

    solve(now, idx + 1, 1, cnt)



for _ in range(T):
    coins = []
    ans = 1000
    for _ in range(3):
        for char in input().split():
            coins.append(True if char == 'T' else False)

    solve(coins, 0, 1, 0)