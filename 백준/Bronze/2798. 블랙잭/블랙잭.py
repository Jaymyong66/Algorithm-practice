[N, M] = list(map(int, input().split()))
nums = list(map(int, input().split()))
answer = 0

for i in range(N):
	for j in range(i+1, N):
		for k in range(j+1, N):
			cur = nums[i] + nums[j] + nums[k]
			if cur > M:
				continue
			if cur == M:
				answer = cur
			else:
				answer = max(cur, answer)
print(answer)