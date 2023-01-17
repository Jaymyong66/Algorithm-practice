

def k_num():
    case = int(input())
    n_list = []
    for i in range(case):
        n, s, e, k = map(int, input().split())
        a = list(map(int, input().split()))
        a = a[s-1:e]
        a.sort()
        print('#',i+1,a[k-1])

def tutor_k_num():
    T = int(input())

    for t in range(T):
        n, s, e, k = map(int, input().split())
        a = list(map(int, input().split()))
        a = a[s-1:e]
        a.sort()
        print("#%d %d" % (t+1, a[k-1]))


if __name__ == '__main__':
    result = k_num()
    print(result)

