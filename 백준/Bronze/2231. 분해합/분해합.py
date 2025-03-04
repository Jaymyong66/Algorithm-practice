N = int(input())
answer = 0

for i in range(1, N):
	string_i = list(map(int, str(i)))
	
	sum_i = sum(string_i) + i


	if N == sum_i:
		answer = i
		break

print(answer)
