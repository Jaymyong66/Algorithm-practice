def nums_sum():
    n, m = map(int, input().split())
    l1 = list(map(int, input().split()))

    p1 = 0
    p2 = 1

    cnt = 0


    while p1 <= n:
        if sum(l1[p1:p2]) == m:
            cnt += 1
            p1 += 1
        elif sum(l1[p1:p2]) < m:
            p2 += 1
        else:
            p1 += 1

    print(cnt)
    return cnt


def nums_sum_best():
    n, m = map(int, input().split())
    l = list(map(int, input().split()))

    p1 = 0
    p2 = 1

    tot = l[0]
    cnt = 0

    while True:
        if tot < m:
            if p2 < n:
                tot += l[p2]
                p2 += 1
            else:
                break
        elif tot == m:
            cnt += 1
            tot -= l[p1]
            p1 += 1

        else:
            tot -= l[p1]
            p1 += 1

    print(cnt)

    return cnt


