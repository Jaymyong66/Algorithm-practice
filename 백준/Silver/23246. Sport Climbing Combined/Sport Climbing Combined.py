num = int(input())
arr = []

for i in range(num):
    row = list(map(int, input().split()))
    arr.append(row)

result = sorted(arr, key=lambda x: (x[1] * x[2] * x[3], x[1] + x[2] + x[3], x[0]))

for name in result[0:3]:
    print(name[0], end=' ')