dices = list(map(int,input().split()))
nums_count = dict()

for i in range(dices[0]):
  for j in range(dices[1]):
    temp = (i+1) + (j+1)
    
    if temp in nums_count:
      nums_count[temp] = nums_count[temp] + 1
    else:
      nums_count[temp] = 1
      
result = [k for k,v in nums_count.items() if max(nums_count.values()) == v]  # ??  max 로만 하면 최대값인 키가 여러개일때 하나만 나옴. 리스트 컴프리헨션으로 해야 여러 키가 나옴.

print(result)

# 정답지
# import sys
# sys.stdin = open("input.txt", "r")
# n, m = map(int,input().split())
# cnt = [0] * (n+m+3)
# max = -2147000000

# for i in range(1, n+1):
#   for j in range(1, m+1):
#     cnt[i+j] += 1 
    
# for i in range(n+m+1):
#   if cnt[i] > max:
#     max = cnt[i]
    
# for i in range(n+m+1):
#   if cnt[i] == max:
#     print(i, end=' ')