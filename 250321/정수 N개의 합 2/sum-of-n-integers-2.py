n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
prefix_sum = [0] * (n+1)
prefix_sum[0] = 0
answer = 0

arr.insert(0,0)

for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

for i in range(1, n - k + 2):
    answer = max(answer, prefix_sum[i+k-1] - prefix_sum[i-1])

print(answer)