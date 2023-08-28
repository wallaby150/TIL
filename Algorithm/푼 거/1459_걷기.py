import sys
input = lambda : sys.stdin.readline().rstrip()



# 집 위치 x, y, 한 블록 소요시간 w, 대각선 소요시간s
x, y, w, s = map(int, input().split())

now_x, now_y = 0, 0

if 2*w < s:
    print(w*(x+y))
else:
    if w < s:
        print(s*min(x,y)+w*(abs(x-y)))
    else:
        z = s * min(x, y)
        c = z
        a = 2*s * (abs(x-y)//2)
        c += a
        b = w * (abs(x-y)%2)
        c += b
        print(c)
