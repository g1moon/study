from datetime import datetime, timedelta

def solution(lines):
    result = []
    for hour in lines :
        temp = hour.split(' ')
        date = str(temp[0]) +" "+str(temp[1])
        if '.' in temp[2] :
            delay = temp[2].split('.')
            delay[1] = delay[1][:-1]
        else :
            delay = list(temp[2][:-1])
            delay += ["0"]
        end = datetime.fromisoformat(date)
        start = end - timedelta(seconds =int(delay[0]),milliseconds = int(delay[1])-1)
        result.append([start,end])
        
    answers = []
    
    for timelist in result :
            for time in timelist :
                answer =0
                for moment in result :
                    comp =False
                    start = time
                    end = time + timedelta(milliseconds =999)

                    if start >= moment[0] and start<= moment[1]:
                        comp = True
                    elif end >= moment[0] and end <= moment[1]:
                        comp = True
                    elif start <= moment[0] and end >= moment[1]:
                        comp = True
                    if comp == True :
                        answer += 1
                answers.append(answer)
    return max(answers)


#!/usr/bin/python
def solution(lines):
    answer = 0

    start = []
    end = []
    for i in lines:
        s = i.split()[1]
        t = float(i.split()[2][:-1])

        # 초 단위로 바꾸기
        ss = list(map(float,s.split(":")))
        end_ts = ss[0] * 3600 + ss[1] * 60 + ss[2]
        end.append(end_ts)

        start_ts  = end_ts - float(t) + 0.001
        start.append(start_ts)
    
    answer = 0
    for i in range(len(lines)):
        total = 1
        for j in range(i+1,len(lines)):
            if start[i] + 1 > start[j] or start[j] < end[i] + 1:
                total += 1
        answer = max(answer,total)
    return answer

solution(lines)