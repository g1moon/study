'''
# 불량사용자 목록을 만들어 -> 당첨처리시 제외 
# 일부 문자를 *로 가려서 전달 
    # 아이디 당 최소 하나 이상의 *
    

'''
def ck(str1, str2):
    if len(str1) == len(str2):
        for i in range(len(str1)):     
            if str1[i] == str2[i]:
                continue
            else:
                #다른데 둘중하나가 *이야 -> continue 
                #다른데 *도아니야 -> return False
                if str1[i] == '*' or str2[i] == '*':
                    continue 
                else:
                    return False
        return True
    else:
        return False

cnt = 0
def solution(user_id, banned_id):

    
    def dfs(idx, ban_idx):
        global cnt
        #다 보고 더해주고 리턴
        if ban_idx == len(banned_id):
            cnt +=1
            return 
        #걍 idx가 높을떄 리턴
        if idx == len(user_id):
            return 
        
        for i in range(idx,len(user_id)):
            # if len(user_id) - i < len(banned_id) - ban_idx :
            #     return 
            
            if ck(user_id[i], banned_id[ban_idx]):
                dfs(i+1, ban_idx +1)
            

    dfs(0,0)
    return cnt