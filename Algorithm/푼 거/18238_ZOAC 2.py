import sys
input = lambda: sys.stdin.readline().rstrip()

nums = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
        'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

now = 0
time = 0

for char in input():
    target = nums[char]
    time += min(abs(target - now), 26 - max(now, target) + min(now, target))
    now = target

print(time)
