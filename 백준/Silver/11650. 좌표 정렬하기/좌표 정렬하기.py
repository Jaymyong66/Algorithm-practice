N = int(input())
arr = []
for i in range(N):
    nums = list(map(int,input().split()))
    arr.append(nums)

result = sorted(arr, key = lambda x : (x[0], x[1]))

for i in result:
    for u in i:
        print(u, end=' ')
    print()


