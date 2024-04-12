import sys
input = lambda : sys.stdin.readline().rstrip()

N, L = map(int, input().split())
boxes = list(map(int, input().split()))
hap = 0


for i in range(N-1, 0, -1):
    cnt = N - i
    hap += boxes[i]
    average = hap / cnt

    if average >= boxes[i-1] + L or average <= boxes[i-1] - L:
        print("unstable")
        break
else:
    print("stable")