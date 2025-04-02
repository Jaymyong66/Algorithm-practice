def solution(s):
    answer = 0
    x = ''
    x_len = 0
    other_len = 0
    
    for char in s:
        if x == '':
            x = char
            x_len = 1
            continue
        
        if char == x:
            x_len += 1
        else:
            other_len += 1
        
        if x_len == other_len:
            answer += 1
            x = ''
            x_len = 0
            other_len = 0
            
    if x_len != 0:
        answer += 1
        
    return answer