def grid_sum():
    n = int(input())
    li = [list(map(int, input().split())) for i in range(n)]

    big = -100000
    c1sum = 0
    c2sum = 0

    for i in range(n):
        rowsum = 0
        colsum = 0
        c1sum += li[i][i]
        c2sum += li[i][n-1-i]

        for j in range(n):
            rowsum += li[i][j]
            colsum += li[j][i]

        if rowsum > big:
            big = rowsum
        elif colsum > big:
            big = colsum
    if c1sum > big:
        big = c1sum
    elif c2sum > big:
        big = c2sum

    print(big)