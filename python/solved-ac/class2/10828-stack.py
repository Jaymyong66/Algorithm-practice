import sys

num = int(sys.stdin.readline())
stack = []

for _ in range(num):
    word = sys.stdin.readline().split()
    cmd = word[0]
    # top = -1

    if cmd == "push":
        stack.append(word[1])
        # top += 1

    elif cmd == "pop":
        # val = stack[top]
        # top -= 1
        if len(stack) == 0:
            print(-1)
        else:
            val = stack.pop()
            print(val)

    elif cmd == "size":
        # print(top + 1)
        print(len(stack))

    elif cmd == "empty":
        # if top > -1:
        #     print(0)
        # else:
        #     print(1)
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif cmd == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
        # print(stack[top])


    # else:
    #     print("error")




