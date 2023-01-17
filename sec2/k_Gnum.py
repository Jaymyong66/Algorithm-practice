def K_Gnum():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    res = set()

    for i in range(n):
        for j in range(i + 1, n):
            for m in range(j + 1, n):
                res.add(a[i] + a[j] + a[m])
    res = list(res)
    res.sort(reverse=True)
    print(res[k - 1])


if __name__ == '__main__':
    K_Gnum()
