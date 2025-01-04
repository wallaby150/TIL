texts = list(input().split())
exceptions = ('i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili')
ans = ''

for i in range(len(texts)):
    text = texts[i]
    if text not in exceptions or i == 0:
        ans += text[0].upper()

print(ans)