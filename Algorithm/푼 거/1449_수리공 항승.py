# 구멍 갯수, 테이프 길이
N, L = map(int, input().split())
points = sorted(list(map(int, input().split())))
start = points[0]
count = 0


for point in points:
    if point - start > L - 1:
        count += 1
        start = point

print(count + 1)