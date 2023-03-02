def sum_two_list():
    N = input()
    first_list = list(map(int, (input().split())))
    #print(first_list)
    M = input()
    second_list = list(map(int, (input().split())))

    result = first_list + second_list
    #print(result)
    result.sort()
    print(result)


def sum_two_list2():
    N = int(input())
    first_list = list(map(int, (input().split())))
    M = int(input())
    second_list = list(map(int, (input().split())))
    result = []

    p1 = 0
    p2 = 0

    while p1 < N and p1 < M:
        if first_list[p1] <= second_list[p2]:
            result.append(first_list[p1])
            p1 += 1
        else:
            result.append(second_list[p2])
            p2 += 1

    if p1 == N:
        result = result + second_list[p2:]
    else:
    # if p2 == M:
        result = result + first_list[p1:]

    # if p1 < N:
    #     result = result + first_list[p1:]
    # #else:
    # if p2 < M:
    #     result = result + second_list[p2:]

    print(result)

def two_sum_3():
    n1 = int(input())
    l1 = list(map(int, input().split()))
    n2 = int(input())
    l2 = list(map(int, input().split()))

    p1 = 0
    p2 = 0
    result = []

    while (p1 < n1 and p2 < n2):
        if l1[p1] < l2[p2]:
            result.append(l1[p1])
            p1 += 1
        else:
            result.append(l2[p2])
            p2 += 1

    if p1 == n1:
        result = result + l2[p2:]
    else:
        result = result + l1[p1:]

    print(result)
    return result




    # 인덱싱을 잘 쓰자.
    # while문 조건식을 잘 쓰자.  true일 때 돌아가는 거다. False이면 끝난다.
    # 리스트에서 +연산과 append의 차이