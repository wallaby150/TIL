import sys
input = lambda: sys.stdin.readline().rstrip()


T = int(input())
for _ in range(T):
    dict = {"TTT": 0, "TTH": 0, "THT": 0, "THH": 0, "HTT": 0, "HTH": 0, "HHT": 0, "HHH": 0}
    text = input()

    for i in range(38):
        dict[text[i:i + 3]] += 1

    print(' '.join(map(str, dict.values())))
