A = input()
B = input()
ans = ''
tmp = ''

for i in range(8):
    ans += A[i] + B[i]

while len(ans) != 2:
    for i in range(len(ans) - 1):
        tmp += str(((int(ans[i]) + int(ans[i + 1])) % 10))
    ans = tmp
    tmp = ''

print(ans)