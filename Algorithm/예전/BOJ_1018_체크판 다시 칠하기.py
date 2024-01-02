def search(start_y, start_x):
    global min_count

    wb = ["W", "B"]
    white_first = 0
    black_first = 0
    # W부터 시작하는 경우를 기준으로 설정
    key = 0
    for check_y in range(8):
        for check_x in range(8):
            # 흰 색이 처음 시작하는 것이
            if wb[key] != base_board[start_y+check_y][start_x+check_x]:
                white_first += 1
            else:
                # 둘이 같다면 B부터 시작하는 경우에 칠한 카운터를 하나 늘려줘야 한다.
                black_first += 1
            key = not key      # 다음 색깔은 달라야 하니까 바꾼다.
        key = not key          # 마지막 색깔과 다음 y축의 첫 색깔이 같아야 함으로 한 번 더 바꾼다.

    min_count = min(min_count, white_first, black_first)


N, M = map(int, input().split())    # 세로, 가로
base_board = list(list(input()) for _ in range(N))
min_count = M*N                     # 칠해야 하난 최소값

for y in range(N-8+1):
    for x in range(M-8+1):
        search(y, x)                # 보드를 만들 수 있는 부분을 모조리 확인

print(min_count)
