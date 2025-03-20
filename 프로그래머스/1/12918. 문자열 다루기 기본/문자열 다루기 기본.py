def solution(s):
    answer = True
    
    if len(s) != 4 and len(s) != 6:
        return False
    
    if not s.isdigit():
        return False
    
    return answer