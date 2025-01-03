N = int(input())

for _ in range(N):
    text = input().lower()
    ans = ''

    for i in range(97, 123):
        if text.find(chr(i)) == -1:
            ans += chr(i)

    if not ans:
        print("pangram")
    else:
        print(f"missing {ans}")
