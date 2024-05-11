S = input()
T = input()

def dfs(text):
    if len(text) == len(S):
        if text == S:
            print(1)
            exit()
        return

    if text[-1] == 'A':
        dfs(text[:-1])
    if text[0] == 'B':
        dfs(text[1:][::-1])
    return


dfs(T)
print(0)
