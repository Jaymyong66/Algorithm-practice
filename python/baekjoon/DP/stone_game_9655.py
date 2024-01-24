def stone_game():
    num = int(input())

    dp = [0 for i in range(num+1)]

    for i in range(1, num+1):
        dp[i] = int(i/3) + int(i%3)
        #print(i, dp[i])

    if dp[num] % 2 == 1:
        print('SK')
    else:
        print('CY')


stone_game()