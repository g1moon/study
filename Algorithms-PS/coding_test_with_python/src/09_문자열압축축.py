#09 문자열 압축

def solution(s):
    res = len(s)
    for basis in range(1, len(s)//2 + 1):
        cnt = 1
        com = ''
        prev = s[:basis]
        
        for i in range(basis, len(s), basis):
            nxt = s[i: i + basis]
            if prev == nxt:
                cnt += 1
            else: #다른 경우 
                if cnt >= 2: #중복된게 존재했던 경우 
                    com = com + str(cnt)
                    com = com + prev
                else: #중복된게 없던 경우 
                    com = com + prev
                prev = nxt
                cnt = 1
        #남아있는 문자 처리 
        if cnt >= 2:
            com += str(cnt) + prev
        else:
            com += prev
        res = min(res, len(com))
            
    return res 

'''
- range(2, len(s)+1)
- 1개 단위로 자르는 것은 : 문자열의 길이 
- 2개부터 확인하고 -> 길이를 l에 저장
- 만약 l > new_l 이면 -> 새롭게 l에 저장
- 인덱싱했는데 -> 에러가나면 -> 그냥 거기부터 끝까지해서 추가 

- 그게 또 나오면 -> +(인덱싱길이+1)
- 아니면 ->  (+인덱싱길이)

'''