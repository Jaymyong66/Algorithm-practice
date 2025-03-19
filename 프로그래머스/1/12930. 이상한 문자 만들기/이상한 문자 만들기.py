def solution(s):
    answer = ''
    cur_idx = 0
    
    for idx, char in enumerate(s):
        if char == ' ':
            cur_idx = 0
            answer += char
        else:
            if cur_idx % 2 == 0:
                answer += char.upper()
                cur_idx += 1
            else:
                answer += char.lower()
                cur_idx += 1
                
    return answer