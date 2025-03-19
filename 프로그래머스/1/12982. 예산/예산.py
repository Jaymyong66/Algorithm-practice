def solution(d, budget):
    answer = 0
    
    d.sort()
    
    for won in d:
        budget -= won
        
        if budget < 0:
            break
        else:
            answer += 1
    
    
    
    return answer