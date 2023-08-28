text = sorted(list(input()), reverse=True)
front = []
back = []
temp = []

while text:
    now = text.pop()
    temp.append(now)
    if 2 <= len(temp):
        if temp[-2] == temp[-1]:
            front.append(temp.pop())
            back.append(temp.pop())

if len(temp) <= 1:
    back.reverse()
    ans = front + temp + back
    print(''.join(map(str, ans)))
else:
    print("I\'m Sorry Hansoo")