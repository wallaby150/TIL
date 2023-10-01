import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
order = []

def solve(o):
    flag = False

    # 단어 첫 글자 확인
    for i in range(len(o)):
        if flag or i == 0:
            if o[i].lower() not in order:
                order.append(o[i].lower())
                return i
            else:
                flag = False

        elif o[i] == ' ':
            flag = True

    # 다른 글자들 확인
    for j in range(len(o)):
        if o[j].lower() not in order and o[j] != ' ':
            order.append(o[j].lower())
            return j

    # 그래도 없음
    return -1


for _ in range(N):
    option = input()
    index = solve(option)
    if index == -1:
        print(option)
    else:
        for k in range(len(option)):
            if k == index:
                print(f"[{option[k]}]", end='')
            else:
                print(option[k], end='')
        else:
            print()