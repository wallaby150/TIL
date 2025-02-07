import sys

while True:
    try:
        line = sys.stdin.readline().rstrip()
        if not line:
            break

        stop_count = 0
        cursor = 0

        for word in line.split():
            if cursor < len(word):
                stop_count += 1
                cursor += 1

        print(stop_count)

    except EOFError:
        break
