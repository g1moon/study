def solution(number, k):
    ans = ''
    res = 0
    num_lst = list(number)
    col = [number[0]] 
    #i를 col에 추가하고 -> col에 모든 루프를 돌며 자기를 뒤로 추가한 것을 어펜드
    for i in range(1,len(number)):
        
        #col의 모든 루프를 돌며 -> i를 뒤로 넣어 어펜드
        for c_idx in range(len(col)):
            item = col[c_idx] + num_lst[i]
            if len(item) > (len(number)-k):
                continue 
            col.append(item)
        col.append(num_lst[i])
        
        
    col = list(map(int, col))
    ans = str(max(col))
    
    return ans
