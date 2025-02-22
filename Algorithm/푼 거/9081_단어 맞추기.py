def next_permutation(word):
    text = list(word)
    n = len(text)

    i = n - 1
    while i > 0 and text[i - 1] >= text[i]:
        i -= 1
    if i == 0:
        return ''.join(text)
    j = n - 1
    while text[i - 1] >= text[j]:
        j -= 1
    text[i - 1], text[j] = text[j], text[i - 1]
    text[i:] = sorted(text[i:])
    return ''.join(text)


T = int(input())
for _ in range(T):
    word = input()
    print(next_permutation(word))
