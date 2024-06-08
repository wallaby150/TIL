T = int(input())

for _ in range(T):
    text = input().replace(' ', '')
    cnt = [0] * 26

    for char in text:
        cnt[ord(char) - 97] += 1

    if cnt.count(max(cnt)) > 1:
        print('?')
    else:
        print(chr(97 + cnt.index(max(cnt))))
