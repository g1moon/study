
def dfs(idx, res):
    global cnt
    if idx >= len(code):
        cnt += 1
        return 
    
    for i in range(1,27):
        if i < 10:      #i <10
            if code[idx] == str(i):
                if res == "":
                    dfs(idx+1, str(i))
                else:
                    dfs(idx+1, res+ "," +str(i))
            
        else:
            try:
                if (code[idx] + code[idx+1]) == str(i):
                    if res == "":
                        dfs(idx+2, str(i))
                    else:
                        dfs(idx+2, res + "," + str(i))
            except:
                pass
            

if __name__ == "__main__":
    #init
    cnt = 0
    #input
    code = input() #str로 받아 
    
    #
    dfs(0,"")
    
    #print
    print(cnt)
    
    
    