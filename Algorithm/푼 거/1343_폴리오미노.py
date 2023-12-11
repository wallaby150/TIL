import sys
input = lambda : sys.stdin.readline().rstrip()

text = input()
answer = ''


def poly(l):
    global answer

    if l % 2:
        return False

    while l:
        if l >= 4:
            l -= 4
            answer += 'AAAA'
        else:
            l -= 2
            answer += 'BB'
    return True


def solve():
    global answer
    tmp = 0

    for char in text:
        if char == '.':
            if tmp:
                if poly(tmp) == False:
                    return -1
                tmp = 0
            answer += '.'
        else:
            tmp += 1
    else:
        if tmp:
            if poly(tmp) == False:
                return -1

    return answer


print(solve())