code = input()
answer = [1, 1]

if code[0] == '0':
    print(0)
    exit()

for i in range(1, len(code)):
    temp = code[i-1] + code[i]

    if code[i] == '0':
        if int(code[i-1]) > 2:
            print(0)
            exit()
        elif temp == '00':
            print(0)
            exit()

    elif i < len(code)-1 and code[i+1] == '0':
        answer.append(answer[-1])

    elif int(temp) > 26 or '0' in (code[i-1], code[i]):
        answer.append(answer[-1])

    else:
        answer.append(answer[-1] + answer[-2])

print(answer[-1] % 1000000)