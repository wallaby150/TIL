words = list(input() for _ in range(5))
for i in range(15):
    for word in words:
        if len(word) > i:
            print(word[i], end='')