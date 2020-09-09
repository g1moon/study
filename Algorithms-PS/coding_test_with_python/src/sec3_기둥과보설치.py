import copy
#################
#input-----------------------------------
n = 5
#input1
# build_frame=[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
#input2
build_frame=[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
#---check--------------------------------------------------------
def check(res):
    for res_lst in res:
        x, y, a = res_lst
        #a가 0인경우 - 기둥
        if a == 0:
            if (y == 0) or [x,y,1] in res or [x-1,y,1] in res or [x,y-1,0] in res:
                continue 
            else:
                print(res_lst)
                return False 
        #a가 1인경우 - 보
        elif a == 1:
            if [x+1,y-1, 0] in res or [x, y-1, 0] in res:
                continue 
            elif [x-1, y, 1] in res and [x+1, y, 1] in res:
                continue 
            else:
                print(res_lst)
                return False 
    return True 
    
# res = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
# print(check(res))
#-------------solution---------------------------------------
def solution(n, build_frame):
    import copy

    res = []
    
    for info_lst in build_frame:
        x, y, a, b = info_lst
        tmp_res = copy.deepcopy(res)
        #설치
        if b == 1:
            tmp_res.append([x,y,a]) #설치
            if check(tmp_res): #맞으면
                res.append([x,y,a])
            else:
                continue
        #삭제 
        else:
            del tmp_res[tmp_res.index([x,y,a])]
            if check(tmp_res):
                del res[res.index([x,y,a])]
            else:
                continue 
            
    res = sorted(res, key = lambda x: (x[0], x[1], x[2]))
    return res
# -------------------------------------------------
print(solution(n, build_frame))