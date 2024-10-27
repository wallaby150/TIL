while True:
    try:
        N = int(input())
    except:
        break

    now = 1
    ans = 1
    while True:
        if now % N != 0:
            now = now * 10 + 1
            ans += 1
        else:
            print(ans)
            break
