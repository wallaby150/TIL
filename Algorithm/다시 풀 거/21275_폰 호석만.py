A, B = input().split()
x, a, b = 0, 0, 0
cnt = 0

for i in range(2, 37):
    try:
        tmp_a = int(A, i)
    except:
        continue

    for j in range(2, 37):
        try:
            tmp_b = int(B, j)
            if tmp_a == tmp_b:
                cnt += 1
                x = tmp_a
                a = i
                b = j
        except:
            continue
print(cnt)
if cnt == 0:
    print("Impossible")
elif cnt == 1:
    print(x, a, b)
else:
    print("Multiple")
