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

