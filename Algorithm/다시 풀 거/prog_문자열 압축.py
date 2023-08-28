import sys
input = lambda : sys.stdin.readline().rstrip()


def solution(s):
    result = []

    if len(s) == 1:
        return 1

    for i in range(1, len(s)//2 + 1):
        word = ''
        count = 1
        temp = s[:i]

        for j in range(i, len(s)+i, i):
            if temp == s[j:i+j]:
                count += 1
            else:
                if count == 1:
                    word += temp
                else:
                    word += str(count) + temp
                temp = s[j:i+j]
                count = 1
        result.append(len(word))

    return min(result)

print(solution('aabbaccc'))