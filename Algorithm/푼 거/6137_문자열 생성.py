import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
S = []
answer = ''
for _ in range(N):
    S.append(input())

s = 0
e = N-1

while s <= e:
    left, right = S[s], S[e]

    if left > right:
        answer += right
        e -= 1
    elif left < right:
        answer += left
        s += 1

    # left와 right가 같다면
    else:
        inner_s = s + 1
        inner_e = e - 1
        flag = 0

        while inner_s <= inner_e:
            # inner_left, inner_right
            il, ir = S[inner_s], S[inner_e]
            if il > ir:
                flag = 1
                break
            elif il < ir:
                flag = 2
                break
            inner_s += 1
            inner_e -= 1

        if flag == 0:
            answer += left
            s += 1
        elif flag == 1:
            answer += right
            e -= 1
        else:
            answer += left
            s += 1

for i in range(0, len(answer), 80):
    print(answer[i:i+80])
