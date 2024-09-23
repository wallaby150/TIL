import sys
input = lambda: sys.stdin.readline().rstrip()

# 학생 수, 졸고 있는 학생수 K, 출석 코드를 보낼 학생수 Q, 주어질 구간의 수 M
N, K, Q, M = map(int, input().split())
snooze_student = set(map(int, input().split()))
received_student = list(map(int, input().split()))

check = [True] * 3 + [False] * N
for code in received_student:
    if code in snooze_student:
        continue

    now = code
    while now <= N + 2:
        if now not in snooze_student:
            check[now] = True
        now += code

hap = [0] * 3
for i in range(3, N+3):
    hap.append(hap[-1] + (0 if check[i] else 1))

for _ in range(M):
    a, b = map(int, input().split())
    print(hap[b] - hap[a-1])
