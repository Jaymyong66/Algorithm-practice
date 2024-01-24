
def Kfun():
    N, K = map(int, input().split())
    q_list = []

    for i in range(1, N+1):
        if N % i == 0:
            q_list.append(i)

    if len(q_list) < K:
        return -1

    return q_list[K-1]

def tutor_Kfun():
    n,k = map(int,input().split())
    cnt = 0

    for i in range(1, n+1):
        if n%i ==0:
            cnt+=1
        if cnt==k:
            print(i)
            break
    else:
        print(-1)


