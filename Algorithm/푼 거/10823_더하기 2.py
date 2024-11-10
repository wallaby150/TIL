texts = ''
while True:
    try:
        texts += input()
    except:
        break

print(sum(map(int, texts.split(','))))
