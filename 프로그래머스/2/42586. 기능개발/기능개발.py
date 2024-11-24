from math import ceil

def solution(progresses, speeds):
    # 작업 완료 예상 날짜 계산
    completion_days = [
        ceil((100 - progress) / speed)
        for progress, speed in zip(progresses, speeds)
    ]
    
    # 배포 처리
    answer = []
    current_max_day = completion_days[0]
    count = 0

    for day in completion_days:
        if day <= current_max_day:
            count += 1
        else:
            answer.append(count)
            current_max_day = day
            count = 1
    
    # 마지막 배포 처리
    answer.append(count)
    
    return answer
