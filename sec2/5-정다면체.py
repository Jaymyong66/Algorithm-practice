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

