num = int(input())
scores = list(map(int,input().split()))
sum = 0
mean = 0
min = 2147000000

for i in range(num):
  sum += scores[i]
  
mean = int((sum / num) + 0.5) # 소수점 첫째 자리에서 반올림

for idx, x in enumerate(scores):
  temp = abs(x-mean)
  if temp < min:
    min = temp
    score = x
    res=idx+1
    
  elif temp == min:
    if x > score:
      score = x
      res = idx+1
      
print(mean, res)
    


#round 함수 , sum 함수
# round 함수는 round_half_even 방식이다.(올림이 일어날 때, 짝수쪽으로 붙는다.)
# 우리가 원하는건 round_half_up 방식.
# 그럼 a = a+0.5  방식으로 올림을 한다.












# def represent_num():
#     num = int(input())
#     score = list(map(int,input().split()))
#     mean = 0
#     temp = 100

#     for i in score:
#         mean += i
#     mean /= len(score)

#     for j in range(len(score)):
#         a = abs(mean-score[j])
#         b = -1
#         idx = 0
#         if a < temp:
#             temp = a
#             idx = j
#             if score[j] > b:
#                 b = score[j]
#                 idx = j

#     return idx



# if __name__ == '__main__':
#     print(represent_num())
