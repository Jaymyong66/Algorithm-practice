def card_reverse():
    card = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    for i in range(10):
        a, b = map(int, input().split())
        # for j in range(((b-a)+1 // 2)):
        #     card[a-1], card[b-1] = card[b-1], card[a-1]
        #     a += 1
        #     b -= 1
        for j in range(((b-a)+1 // 2)):
            card[a-1+i], card[b-1+i] = card[b-1], card[a-1]
            a += 1
            b -= 1

    print(card)

# error..?

