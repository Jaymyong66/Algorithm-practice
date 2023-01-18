def only_number():
    s = input()
    temp = ''
    min = 1  # 1과 나눠지는 자기 자신인 약수 ex) 28
    min2 = 0

    for i in s:
        if i.isdigit():
            temp += i

    temp = int(temp)

    # 처음에 내가 한 것.
    # for i in range(temp//2):
    #     # print(temp % (i + 1))
    #     if temp % (i+1) == 0:
    #         min +=1

    for i in range(temp):
        if temp % (i+1) == 0:
            min2 += 1

    print(temp)
    print(min2)

# 약수는 나누어 떨어지는 것.


def only_number_good():
    s = input()
    res = 0

    for x in s:
        if x.isdeciaml():
            res = res*10+int(x)

    print(res)
    cnt = 0
    for i in range(1, res+1):
        if res % i == 0:
            cnt += 1
    print(cnt)