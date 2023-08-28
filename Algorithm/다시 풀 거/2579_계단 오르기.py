import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
stairs = [0]

for _ in range(N):
    stairs.append(int(input()))

highest = 0

def climbing (now, score, count):
    global highest

    if now <= N:
        score += stairs[now]
    else:
        return

    if count == 2:
        return

    # 최고값 갱신
    if now == N:
        highest = max(highest, score)

    climbing(now+1, score, count+1)
    climbing(now+2, score, 0)

climbing(0, 0, 0)
print(highest)