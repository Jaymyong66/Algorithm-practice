N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())))

sum = 0
for i in range(N):
	sum += A[i] * B[i]

print(sum)
