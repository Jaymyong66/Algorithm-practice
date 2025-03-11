N = int(input())
A = set(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

for num in nums:
    print(1 if num in A else 0)