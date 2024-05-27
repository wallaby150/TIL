text = list(input().split(':'))
if text[0] == '':
    text = text[1:]
elif text[-1] == '':
    text = text[:-1]

ans = []
for word in text:
    if word == '':
        for _ in range(8-len(text)+1):
            ans.append('0000')
    else:
        ans.append('0' * (4 - len(word)) + word)

print(':'.join(ans))
