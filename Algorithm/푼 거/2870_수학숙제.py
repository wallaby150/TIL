import sys
input = lambda : sys.stdin.readline().rstrip()

num_list = []
for _ in range(int(input())):
    text = input()

    temp = ''

    for char in text:
        if char.isdigit():
            temp += char
            # print(temp)
        else:
            if temp:
                num_list.append(int(temp))
                temp = ''
    else:
        if temp:
            num_list.append(int(temp))
            temp = ''


for num in sorted(num_list):
    print(num)