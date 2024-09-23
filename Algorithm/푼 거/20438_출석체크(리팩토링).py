import sys
input = lambda: sys.stdin.readline().rstrip()

# 학생 수, 졸고 있는 학생수 K, 출석 코드를 보낼 학생수 Q, 주어질 구간의 수 M
N, K, Q, M = map(int, input().split())
snooze_student = set(map(int, input().split()))  # 졸고 있는 학생 집합
received_student = list(map(int, input().split()))  # 출석 코드를 받은 학생 리스트

# 출석 체크를 위한 누적 합 배열 초기화
hap = [0] * (N + 3)

# 출석 체크 로직
for code in received_student:
    if code in snooze_student:
        continue  # 졸고 있는 학생은 건너뛰기
    for i in range(code, N + 3, code):
        if i not in snooze_student:
            hap[i] = 1  # 출석한 학생 표시

# 누적 합 계산
for i in range(3, N + 3):
    hap[i] += hap[i-1]

# 구간별 출석하지 않은 학생 수 계산 및 출력
for _ in range(M):
    a, b = map(int, input().split())
    print(b - a + 1 - (hap[b] - hap[a-1]))  # 총 학생 수 - 출석한 학생 수