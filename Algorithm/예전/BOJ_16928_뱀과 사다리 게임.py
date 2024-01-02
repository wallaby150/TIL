ladders_n, snakes_n = map(int, input().split())         # 사다리와 뱀의 수를 각각 저장합니다.
ladders_dict = dict(list(map(int, input().split())) for _ in range(ladders_n))
snakes_dict = dict(list(map(int, input().split())) for _ in range(snakes_n))

# 처음에는 아래와 같은 방법으로 dict형식으로 바꿨는데, [key, value] 형식으로 이중 리스트로 저장된 것을 곧바로 형변환 할 수 있었습니다.
# ladders_list = list(list(map(int, input().split())) for _ in range(ladders_n))
# snakes_list = list(list(map(int, input().split())) for _ in range(snakes_n))
# ladders_dict = {ladder[0] : ladder[1] for ladder in ladders_list}
# snakes_dict = {snake[0] : snake[1] for snake in snakes_list}


now_nums = [[1,0]]              # BFS 형식으로 탐색하기 위해서 현재 위치와 주사위를 굴린 횟수를 저장하는 리스트를 저장하는 이중 리스틀 만듭니다.
# roll_count = 0
reached = False

while not reached:              # or != 100?
    # roll_count += 1
    while now_nums:
        now_num, roll_count = now_nums.pop(0)
        trigger = False
        for possible in range(now_num+6, now_num, -1):
            if possible >= 100:
                reached = True
                answer = roll_count + 1
                break
            if possible in ladders_dict.keys():
                now_nums.append([ladders_dict[possible], roll_count+1])
            elif possible in snakes_dict.keys():
                now_nums.append([snakes_dict[possible], roll_count + 1])
            elif not trigger:
                now_nums.append([possible, roll_count+1])
                trigger = True
        if reached:
            break

print(answer)

# 뱀이 있으면 피해가야해!!!