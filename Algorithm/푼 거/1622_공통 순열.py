# import sys
# input = lambda : sys.stdin.readline().rstrip()
from collections import deque

try:
    while True:
        a = deque(sorted(input()))
        b = deque(sorted(input()))

        ans = ''

        while a and b:
            if a[0] == b[0]:
                ans += a.popleft()
                b.popleft()
            else:
                if a[0] < b[0]:
                    a.popleft()
                else:
                    b.popleft()

        print(ans)

except:
    pass