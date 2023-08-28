import sys
input = lambda : sys.stdin.readline().rstrip()

S = input()

ans = ''
i = 0

while i < len(S):
    l = S[i:]

    # 공백이 있으면
    if ' ' in l:
        blank_index = l.index(' ')
    else:
        blank_index = 1000001

    # 태그가 있으면
    if '<' in l:
        tag_index = l.index('<')
    else:
        tag_index = 1000001


    # 공백과 태그 중에 먼저 나오는 거 판단
    # 공백이 먼저 나오면
    if blank_index < tag_index:
        ans += l[:blank_index][::-1] + ' '
        i += blank_index + 1
    elif blank_index > tag_index:
        tag_index2 = l.index('>')
        ans += l[:tag_index][::-1] + l[tag_index:tag_index2+1]
        i += tag_index2 + 1

    # 둘 다 없으면
    else:
        ans += l[::-1]
        break

print(ans)