import sys
# sys.stdin = open("input.txt")

from collections import deque

for _ in range(int(input())):
    # func = input().strip("RR") 이건 안 되는 듯
    func_list = input().replace("RR", "")
    n = int(input())

    txt = input()
    try:
        array = deque(map(int, txt.strip("[""]").split(",")))
        # print(array)
    except:
        array = deque()

    for func in func_list:
        if func == "R":
            array.reverse()
        elif func == "D":
            if array == deque():
                print("error")
                break
            else:
                array.popleft()
    else:
        print('[' + ','.join(map(str, array)) + ']')
        # print(list(array))

'''
[2,1]
error
[1,2,3,5,8]
error
'''