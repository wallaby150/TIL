text = input()

if text[1] == '0':
    print(10 + int(text[2:]))
else:
    print(int(text[0]) + int(text[1:]))
