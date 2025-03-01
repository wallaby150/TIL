N = int(input()) - 1
x, y = divmod(N, 14)

lyrics = ['baby', 'sukhwan', 'tururu', 'turururu', 'very', 'cute',
          'tururu', 'turururu', 'in', 'bed', 'tururu', 'turururu', 'baby', 'sukhwan']

if 'tururu' in lyrics[y]:
    cnt = 2 + x - (y % 2)
    if cnt >= 5:
        print(f"tu+ru*{cnt}")
    else:
        print("tu" + "ru" * cnt)
else:
    print(lyrics[y])
