vowels = set('AEIOU')
text = input()

def solve(idx, c, v, check_l):
    # 3연속을 넘어섰다면 안 됨
    if c > 2 or v > 2:
        return 0

    # 마지막에 도달했다면
    if idx == len(text):
        if check_l:
            return 1
        return 0

    tmp = 0

    # 빈칸이라면
    if '_' == text[idx]:
        tmp += solve(idx + 1, c + 1, 0, check_l) * 20
        tmp += solve(idx + 1, c + 1, 0, True)
        tmp += solve(idx + 1, 0, v + 1, check_l) * 5

    # 알파벳이라면
    else:
        # 모음이라면
            if text[idx] in vowels:
                tmp += solve(idx + 1, 0, v+1, check_l)
        # 자음이라면
            else:
                if text[idx] == 'L':
                    tmp += solve(idx + 1, c + 1, 0, True)
                else:
                    tmp += solve(idx + 1, c + 1, 0, check_l)

    return tmp

answer = solve(0, 0, 0, False)
print(answer)
