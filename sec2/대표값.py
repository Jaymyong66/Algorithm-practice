def represent_num():
    num = int(input())
    score = list(map(int,input().split()))
    mean = 0
    temp = 100

    for i in score:
        mean += i
    mean /= len(score)

    for j in range(len(score)):
        a = abs(mean-score[j])
        b = -1
        idx = 0
        if a < temp:
            temp = a
            idx = j
            if score[j] > b:
                b = score[j]
                idx = j

    return idx



if __name__ == '__main__':
    print(represent_num())
