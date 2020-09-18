# import time
# print(time.strftime("%H:%M:%S", time.gmtime(405)))

def time_to_sec(time):
    
    a = time.split(':')
    h,m,s = int(a[0]), int(a[1]), int(a[2])
    sec =0
    sec += (h * 60 * 60)  
    sec += (m * 60) 
    sec += s
    return sec

def sec_to_time(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    a = str(h)
    if len(a) == 1:
        a = '0' + a
    return "%s:%02d:%02d" % (a, m, s)
    

def solution(play_time, adv_time, logs):
    ans = ''
    res = [0] * (time_to_sec(play_time) + 1)
    dic = {}
    
    
    for log in logs:
        s, e = list(map(str,log.split('-')))
        s, e = time_to_sec(s), time_to_sec(e)
        for i in range(s, e):
            res[i] += 1
    #------------------------------------------------
    
    a = sorted(logs)
    a = a[0].split('-')[0]
    a = time_to_sec(a)
    print(a)
    
    for start in range(a, time_to_sec(play_time) - time_to_sec(adv_time) + 1):
        s, e = start, start + time_to_sec(adv_time)
        cnt = 0
        for i in range(s, e):
            cnt += (1 *res[i])
        
        dic[start] = sec_to_time(cnt)
    
    dic  = sorted(dic.items(), key = (lambda x: x[1]), reverse = True)
    ans = sec_to_time(dic[0][0])
    
    return ans






#------------------------------------------------------    

play_time = "02:03:55"
adv_time = "00:14:15"
logs = 	["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
print(solution(play_time, adv_time, logs))
