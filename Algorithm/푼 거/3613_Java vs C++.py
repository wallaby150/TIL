name = input()

# 에러 항목
if name[0] == '_' or name[-1] == '_' or '__' in name:
    print("Error!")

# C++이라면
elif name.lower() == name:
    tmp = ''
    up = False
    for char in name:
        if char == '_':
            up = True
        else:
            if up:
                tmp += char.upper()
                up = False
            else:
                tmp += char

    print(tmp)

# 자바라면
elif name[0] == name[0].lower() and '_' not in name and ' ' not in name:
    tmp = ''

    for char in name:
        if char.isupper():
            tmp += '_' + char.lower()
        else:
            tmp += char

    print(tmp)

else:
    print("Error!")