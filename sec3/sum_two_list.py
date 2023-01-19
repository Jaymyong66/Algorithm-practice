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




    # 인덱싱을 잘 쓰자.
    # while문 조건식을 잘 쓰자.  true일 때 돌아가는 거다. False이면 끝난다.