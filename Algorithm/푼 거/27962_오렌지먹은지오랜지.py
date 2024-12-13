N = int(input())
text = input()
ans = 'NO'

for i in range(1, N):
    left = text[:i]
    right = text[N - i:]
    cnt = 0

    for j in range(len(left)):
        if left[j] != right[j]:
            cnt += 1
            if cnt >= 2:
                break
                
    if cnt == 1:
        ans = 'YES'
        break

print(ans)
