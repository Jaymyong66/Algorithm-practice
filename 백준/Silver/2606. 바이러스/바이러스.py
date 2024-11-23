N = int(input())
E = int(input())

graph = [[] for _ in range(N+1)]

for i in range(E):
	a, b = list(map(int, input().split()))
	graph[a].append(b)
	graph[b].append(a)

visited = [False] * (N+1)

def dfs(node):
	global graph, visited

	if visited[node] == True:
		return

	visited[node] = True

	for v in graph[node]:
		dfs(v)

dfs(1)

print(len([x for x in visited if x == True]) - 1)
