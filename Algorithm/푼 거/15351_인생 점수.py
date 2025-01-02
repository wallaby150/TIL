N = int(input())

for i in range(N):
    text = input()
    score = 0

    for char in text:
        if char == " ":
            continue
        else:
            now = ord(char) - 64
            score += now

    if score == 100:
        print('PERFECT LIFE')
    else:
        print(score)
