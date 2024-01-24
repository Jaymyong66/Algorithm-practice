import sys

def sort_dot():
    num = int(sys.stdin.readline())
    dots = []

    for i in range(num):
        dot = list(map(int, input().split()))
        dots.append(dot)

    dots.sort(key= lambda x:(x[0], x[1]))

    for i in range(num):
        print(dots[i][0], dots[i][1])