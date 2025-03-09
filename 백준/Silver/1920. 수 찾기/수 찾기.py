N = int(input())
A = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

A.sort()

for num in nums:
    left = 0
    # right = M - 1
    right = len(A) - 1
    answer = 0


    while left <= right:
        mid = (right + left) // 2

        if num == A[mid]:
            answer = 1
            break

        if num < A[mid]:
            right = mid - 1

        if num > A[mid]:
            left = mid + 1

    print(answer)
