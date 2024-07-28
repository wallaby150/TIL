N = int(input())
text = input()
cnt = text.count('LL')

if cnt <= 1:
    print(len(text))
else:
    print(len(text) - cnt + 1)
