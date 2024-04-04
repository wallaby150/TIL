import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict

T = int(input())
for _ in range(T):
    tmp = list(map(int, input().split()))
    N = tmp[0]
    nums = tmp[1:]
    d = defaultdict(int)
    for num in nums:
        d[num] += 1
        if d[num] >= N // 2 + 1:
            print(num)
            break
    else:
        print("SYJKGW")
