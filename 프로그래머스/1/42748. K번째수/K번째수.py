def solution(array, commands):
    answer = []
    
    for com in commands:
        [i, j, k] = com
        
        temp = array[i-1:j]
        temp.sort()
        
        answer.append(temp[k-1])
        
    return answer