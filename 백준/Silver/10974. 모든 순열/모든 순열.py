N = int(input())
choose = []
check = [False] * (N + 1)

def pum(level):
    global choose, check, N

    if level == N:
        for u in choose:
            print(u, end=' ')
        print()

    for i in range(1, N+1):
        if check[i] == True:
            continue

        choose.append(i)
        check[i] = True

        pum(level + 1)

        check[i] = False
        choose.pop()

pum(0)