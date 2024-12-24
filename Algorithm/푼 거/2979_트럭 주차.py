A, B, C = map(int, input().split())
time = [0] * 101

for _ in range(3):
    start, end = map(int, input().split())
    for t in range(start, end):
        time[t] += 1

total_fee = 0
for t in time:
    if t == 1:
        total_fee += A
    elif t == 2:
        total_fee += B * 2
    elif t == 3:
        total_fee += C * 3

print(total_fee)
