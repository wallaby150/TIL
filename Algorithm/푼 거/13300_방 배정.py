import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
rooms = [[0] * 2 for _ in range(6)]

for _ in range(N):
    S, Y = map(int, input().split())
    rooms[Y - 1][S] += 1

total_rooms = 0
for grade in range(6):
    for gender in range(2):
        total_rooms += (rooms[grade][gender] + K - 1) // K

print(total_rooms)
