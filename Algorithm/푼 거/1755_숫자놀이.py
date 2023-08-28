import sys
input = lambda : sys.stdin.readline().rstrip()

M, N = map(int, input().split())
nums = {'0':'zero','1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
ans = []

for i in range(M, N+1):
    temp = ''
    for j in str(i):
        temp += nums[j]
    ans.append([i, temp])

ans.sort(key=lambda x: x[1])

for x in range(1, len(ans)+1):
    print(ans[x-1][0], end=" ")
    if x % 10 == 0:
        print()