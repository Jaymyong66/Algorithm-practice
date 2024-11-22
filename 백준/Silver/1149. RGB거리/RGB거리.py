N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]

dp = [[0,0,0] for i in range(N)]

dp[0] = nums[0]

for i in range(1, N):
	dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + nums[i][0]
	dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + nums[i][1]
	dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + nums[i][2]

print(min(dp[N-1]))