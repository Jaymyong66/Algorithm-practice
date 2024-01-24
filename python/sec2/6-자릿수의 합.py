def digit_sum(x):
  x = list(str(x))
  sum = 0
  
  for i in x:
    sum += int(i)
    
  return sum


num = int(input())
values = list(map(int,input().split()))

val_dict = {}
for i in range(num):
  temp = digit_sum(values[i])
  val_dict[values[i]] = temp
  
result = [k for k, v in val_dict.items() if max(val_dict.values()) == v]
  
print(result[0])

# # 정답
# import sys
# sys.stdin=open("input.txt", "r")
# n = int(input())
# a = list(map(int, input().split()))

# def digit_sum(x):
#   sum = 0
#   while x > 0:
#     sum += x % 10
#     x = x // 10
    
#   return sum

# max = -2147000000
# for x in a:
#   tot = digit_sum(x)
#   if tot > max:
#     max = tot
#     res = x
    
# print(res)
  
  
# 파이썬으로 문자열 식으로 처리하는 방법
# for i in str(x):
#   sum += int(i)