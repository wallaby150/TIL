def solve(start, time):
    start_h, start_m = map(int, start.split(":"))
    start_minutes = start_h * 60 + start_m
    end_minutes = start_minutes + time

    fee = 0

    while start_minutes < end_minutes:
        current_minute = start_minutes % 1440  # 하루(1440분) 기준으로 순환
        if 420 <= current_minute < 1140:  # 낮 시간대 (07:00 ~ 19:00)
            fee += min(end_minutes - start_minutes, 1140 - current_minute) * 10
            start_minutes += 1140 - current_minute
        else:  # 밤 시간대
            if current_minute < 420:  # 00:00 ~ 06:59
                fee += min(end_minutes - start_minutes, 420 - current_minute) * 5
                start_minutes += 420 - current_minute
            else:  # 19:00 ~ 23:59
                fee += min(end_minutes - start_minutes, 1440 - current_minute) * 5
                start_minutes += 1440 - current_minute

    return fee


N = int(input())
ans = 0

for _ in range(N):
    now, time = input().split()
    ans += solve(now, int(time))

print(ans)
