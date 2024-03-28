A, B = input().split()
x, a, b = 0, 0, 0


def solve():
    global x, a, b
    cnt = 0


    for i in range(2, 37):
        try:
            tmp_a = int(A, i)
        except:
            continue

        for j in range(2, 37):
            if i == j:
                continue

            try:
                tmp_b = int(B, j)
                if tmp_a == tmp_b:
                    cnt += 1
                    if cnt >= 2:
                        return 2
                    x = tmp_a
                    a = i
                    b = j
            except:
                continue
    return cnt


ans = solve()

if ans == 0:
    print("Impossible")
elif ans == 1:
    print(x, a, b)
else:
    print("Multiple")
