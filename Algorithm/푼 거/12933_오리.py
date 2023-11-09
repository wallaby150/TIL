sound = input()
count = 0
d = {'q': 0, 'u': 0, 'a': 0, 'c': 0, 'k': 0}

for char in sound:
    if char == 'q':
        d['q'] += 1
    elif char == 'u':
        if d['q'] == 0:
            print(-1)
            exit()
        d['q'] -= 1
        d['u'] += 1
    elif char == 'a':
        if d['u'] == 0:
            print(-1)
            exit()
        d['u'] -= 1
        d['a'] += 1
    elif char == 'c':
        if d['a'] == 0:
            print(-1)
            exit()
        d['a'] -= 1
        d['c'] += 1
    elif char == 'k':
        if d['c'] == 0:
            print(-1)
            exit()
        d['c'] -= 1
        d['k'] += 1

        count = max(count, sum(d.values()) - d['k'] + 1)

if sum(d.values()) - d['k'] != 0:
    print(-1)
else:
    print(count)
