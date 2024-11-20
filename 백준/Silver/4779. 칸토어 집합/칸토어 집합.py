def recursive(k):
    if k == 0:
        print('-', end='')
        return

    recursive(k-1)
    print(' ' * (3 ** (k-1)), end='')
    recursive(k-1)

while True:
    try:
        N = int(input())
        recursive(N)
        print()

    except:
        break