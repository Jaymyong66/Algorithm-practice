def combination(index, level, N, lst):
    if level == 6:
        for u in choose:
            print(u,end=' ')
        print()

        return

    for i in range(index, N): 
        choose.append(lst[i]) 
        combination(i+1, level+1, N, lst) 
        choose.pop() 

while True:
    try:
        choose = []
        inputs = list(map(int, input().split(' ')))

        combination(0, 0, inputs[0], inputs[1:])
        print()

        if inputs[0] == 0:
            break

    except:
        break
