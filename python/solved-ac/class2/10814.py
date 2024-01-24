import sys
num = int(input())
lst = []

for i in range(num):
  temp = list(sys.stdin.readline().split())
  
  lst.append(temp)
  

lst.sort(key = lambda x : int(x[0]))

for i in range(num):
  print(lst[i][0], lst[i][1])
  