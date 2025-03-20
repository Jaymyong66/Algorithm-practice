def solution(price, money, count):
    answer = -1
    total = 0
    
    for i in range(1, count + 1):
        total += i * price
    
    if money > total:
        return 0
    else:
        return total - money