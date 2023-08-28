import sys
sys.stdin = open('11403_경로 찾기.txt')
input : lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    N = int(input())


'''
1 1 1
1 1 1
1 1 1

1 0 1 1 1 1 1
0 0 1 0 0 0 1
0 0 0 0 0 0 0
1 0 1 1 1 1 1
1 0 1 1 1 1 1
0 0 1 0 0 0 1
0 0 1 0 0 0 0
'''