# ROT13 변환에 필요한 사전을 미리 생성
rot13 = {'a': 'e', 'i': 'o', 'y': 'u', 'e': 'a', 'o': 'i', 'u': 'y',
         'b': 'p', 'p': 'b', 'k': 'v', 'v': 'k', 'x': 'j', 'j': 'x',
         'z': 'q', 'q': 'z', 'n': 't', 't': 'n', 'h': 's', 's': 'h',
         'd': 'r', 'r': 'd', 'c': 'l', 'l': 'c', 'w': 'm', 'm': 'w',
         'g': 'f', 'f': 'g'}

while True:
    try:
        text = input()
        ans = ''

        for char in text:
            if char.lower() in  rot13:
                if char.islower():
                    ans += rot13[char]
                else:
                    ans += rot13[char.lower()].upper()
            else:
                ans += char

        print(ans)
    except:
        break
