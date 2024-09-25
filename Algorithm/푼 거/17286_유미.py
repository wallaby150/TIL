import sys, math
input = lambda: sys.stdin.readline().rstrip()
from itertools import permutations


# 두 점 사이의 거리를 계산하는 함수
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


yumi = list(map(int, input().split()))

people = [list(map(int, input().split())) for _ in range(3)]

min_distance = float('inf')

for path in permutations(people):
    current = yumi
    total_distance = 0
    for person in path:
        total_distance += distance(current, person)
        current = person
    min_distance = min(min_distance, total_distance)

print(int(min_distance))
