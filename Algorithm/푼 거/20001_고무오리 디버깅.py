import sys
input = lambda : sys.stdin.readline().rstrip()

input()
cnt = 0
while True:
    word = input()

    if word == "문제":
        cnt += 1
    elif word == "고무오리":
        if cnt:
            cnt -= 1
        else:
            cnt += 2
    else:
        if cnt:
            print("힝구")
            break
        else:
            print("고무오리야 사랑해")
            break