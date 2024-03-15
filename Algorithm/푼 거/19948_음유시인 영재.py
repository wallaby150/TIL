texts = list(input().split())
space = int(input())

if space < len(texts)-1:
    print(-1)
else:
    title = "".join(text[0].upper() for text in texts)
    texts.append(title)
    keys = list(map(int, input().split()))

    for text in texts:
        left = ''
        for char in text:
            char = char.lower()
            if left != char:
                keys[ord(char)-97] -= 1
                left = char
                if keys[ord(char)-97] < 0:
                    print(-1)
                    exit()

    print(title)