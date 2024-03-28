import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    text = input()
    if text == text[::-1]:
        print(0)
        continue

    l, r = 0, len(text) - 1
    while l < r:
        if text[l] == text[r]:
            l += 1
            r -= 1

        else:
            tmp1 = text[:l] + text[l+1:]
            tmp2 = text[:r] + text[r+1:]
            if tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]:
                print(1)
            else:
                print(2)
            break