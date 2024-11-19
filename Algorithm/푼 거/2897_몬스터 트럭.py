R, C = map(int, input().split())
parking = [input() for _ in range(R)]

counts = [0] * 5  # 부수는 차의 개수에 따른 주차 가능 공간 수

for i in range(R - 1):
    for j in range(C - 1):
        space = parking[i][j] + parking[i][j+1] + parking[i+1][j] + parking[i+1][j+1]
        cars = space.count('X')
        if '#' not in space:
            counts[cars] += 1

for count in counts:
    print(count)