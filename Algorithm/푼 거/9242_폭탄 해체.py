import sys
input = lambda : sys.stdin.readline().rstrip()

zero = ['***','* *','* *','* *','***']
one = ['  *','  *','  *','  *','  *']
two = ['***','  *','***','*  ','***']
three = ['***','  *','***','  *','***']
four  = ['* *','* *','***','  *','  *']
five = ['***','*  ','***','  *','***']
six = ['***','*  ','***','* *','***']
seven = ['***','  *','  *','  *','  *']
eight = ['***','* *','***','* *','***']
nine = ['***','* *','***','  *','***']
nums = [zero,one,two,three,four,five,six,seven,eight,nine]

text = [input() for _ in range(5)]

tmp = text[0]
l = len(tmp) // 4 + 1

code = ''
codes = [[] for _ in range(l)]

for line in range(5):
    for i in range(l):
        tmp = text[line][i*4:i*4+3]
        while len(tmp) < 3:
            tmp += ' '
        codes[i].append(tmp)

for line in codes:
    if line not in nums:
        ans = "BOOM!!"
        break
    code += str(nums.index(line))
else:
    if int(code) % 6 == 0:
        ans = "BEER!!"
    else:
        ans = "BOOM!!"

print(ans)

