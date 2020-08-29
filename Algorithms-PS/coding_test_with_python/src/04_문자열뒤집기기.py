in_str = input()

#모두 0으로 바꾸는 경우 
#무한루프에서 
#idx를 맨 처음 0으로 잡아주고, 
#1이나오면 ->cnt늘리고 -> 1이 나오지 않을때까지 반복문을 돌려줘 -> 
#그리고 그 idx에서부터 다시 1을 찾아 
cnt = 0
idx = 0
while True:
    if idx == len(in_str):
        break 
    
    if in_str[idx] == '1':
        cnt += 1
        idx += 1
        while True:
            cur_num = in_str[idx]
            if cur_num == '0':
                break  #그럼 idx가 바뀌는 부분 시작점으로 잡힘
            else:
                idx += 1   
    else:
        idx += 1
print(cnt)
################################
#모두 1로 바꾸는 경우
cnt = 0
idx = 0
while True:
    if idx == len(in_str):
        break 
    
    if in_str[idx] == '0':
        cnt += 1
        idx += 1
        while True:
            if idx == len(in_str):
                break 
            cur_num = in_str[idx]
            if cur_num == '1':
                break  #그럼 idx가 바뀌는 부분 시작점으로 잡힘
            else:
                idx += 1   
    else:
        idx += 1
print(cnt)