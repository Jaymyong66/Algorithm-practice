import sys

num = int(input())
words = []

for _ in range(num):
  word = sys.stdin.readline().strip()
  
  words.append(word)

words = set(words)
words = list(words)

words.sort()
words.sort(key=len)
  
# for i in range(num):
#   if i+1 == num:
#     break
#   if len(words[i]) > len(words[i+1]):
#     temp = words[i]
#     words[i] = words[i+1]
#     words[i+1] = temp

for i in words:
  print(i)
  


