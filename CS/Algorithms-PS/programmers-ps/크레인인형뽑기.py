def solution(board, moves):
    answer = 0
    res = []
    '''
    좌우로 움직여 -> 가장 위에있는 인형 잡아
    바구니(stack) -> 같은 거 연속이면 -> 터짐 
    인형이 없는 곳에 집으면 -> 아무일도없음
    
    board : 2차원배열
    moves : 크레인 작동 위치 배열 
    return : 인형의 개수 
    
    크레인은 -> col(moves)에 따라 -> 해당 컬럼의 인형을 뽑아 
    -> 뽑으면 -> 해당 열에 -> 위에서부터(row가 거꾸로) 0이아닌거
    '''
    for move in moves:
        for row in range(len(board)):
            if board[row][move-1] != 0:
                res.append(board[row][move-1])
                board[row][move-1] = 0
                break 
    
    cnt = 0
    remain = True
    while remain:
        for i in range(len(res)-1):
            if res[i] == res[i+1]:
                res[i], res[i+1] = 0, 0
                cnt += 2
                break 
        else:
            remain = False
        
        while 0 in res:
            res.pop(res.index(0))
        
    
    
    answer = cnt
        
                
    
    
    return answer
