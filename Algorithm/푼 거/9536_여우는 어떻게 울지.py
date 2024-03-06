T = int(input())
for _ in range(T):
    sounds = list(input().split())
    cries = set()

    while True:
        text = input()
        if text == 'what does the fox say?':
            tmp = ''
            for sound in sounds:
                if sound not in cries:
                    tmp += sound + ' '

            print(tmp)
            break

        else:
            cries.add(list(text.split())[2])