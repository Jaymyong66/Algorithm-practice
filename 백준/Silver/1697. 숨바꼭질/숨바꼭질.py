from collections import deque

N, K = map(int, input().split())

q = deque()
visited = [False] * (100000 + 1)

q.append([0, N])
visited[N] = True

while q:
	time, pos = q.popleft()

	if pos == K:
		print(time)
		break

	p1 = pos - 1
	p2 = pos + 1
	p3 = pos * 2

	if (0 <= p1 <= 100000) and (not visited[p1]):
		q.append([time + 1, p1])
		visited[p1] = True

	if (0 <= p2 <= 100000) and (not visited[p2]):
		q.append([time + 1, p2])
		visited[p2] = True

	if (0 <= p3 <= 100000) and (not visited[p3]):
		q.append([time + 1, p3])
		visited[p3] = True

