import sys
input = lambda: sys.stdin.readline().rstrip()

S, E, Q = list(input().split())
# 시간을 분 단위로 저장
def toMinutes(t):
    a, b = map(int, t.split(':'))
    return a*60 + b

S = toMinutes(S)
E = toMinutes(E)
Q = toMinutes(Q)

count = 0
attendee = {}
answer = set()


while True:
    try:
        time, nickname = input().split()
        time = toMinutes(time)

        if nickname in attendee:
            if Q >= time >= E:
                if nickname not in answer:
                    answer.add(nickname)
        else:
            if time <= S:
                attendee[nickname] = [time]
    except:
        break

print(len(answer))