def solution(n):
    answer = 0
    prime = [True for _ in range(n+1)]
    
    prime[0] = False
    prime[1] = False
    
    for i in range(2, int(n ** 1/2) + 1):
        if prime[i] == True:
            start = 2
            
            while (i * start) <= n:
                prime[i*start] = False
                start += 1
    
    answer = len(list(filter((lambda n: n == True), prime)))
    
    return answer