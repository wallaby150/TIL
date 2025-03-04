import sys
input = lambda: sys.stdin.readline().rstrip()

case = 1
while True:
    a = input()
    b = input()

    if a == b == "END":
        break

    result = "same" if sorted(a) == sorted(b) else "different"
    print(f"Case {case}: {result}")
    case += 1
