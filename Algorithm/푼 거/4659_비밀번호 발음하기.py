import sys
input = lambda : sys.stdin.readline().rstrip()

vowels = 'aeiou'

def check(word):
    # 모음 여부 확인
    for char in word:
        if char in vowels:
            break
    else:
        return False
    # any()를 사용할 수도 있다.
    # if not any(char in vowels for char in word):
    #     return False

    # 자/모음 3연속 사용 확인
    for i in range(0, len(word) - 2):
        count = 0
        for j in word[i:i+3]:
            if j in vowels:
                count += 1
        if count == 0 or count == 3:
            return False

        if word[i] == word[i+1]:
            if word[i] not in 'eo':
                return False

    if len(word) >= 2:
        if word[-2] == word[-1]:
            if word[-2] not in 'eo':
                return False

    return True

while True:
    test_word = input()

    if test_word == 'end':
        break

    ans = check(test_word)

    if ans:
        print(f"<{test_word}> is acceptable.")
    else:
        print(f"<{test_word}> is not acceptable.")
