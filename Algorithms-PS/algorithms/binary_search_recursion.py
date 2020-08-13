def sequential_search(search_list, num):
    # Code here #
    # 리스트 형태로 리턴 num과 겹치는거 없으면 return empty 
    # 디센딩오더되어있다고 가정  -> 바이너리는 재귀로
    ret = []
    for i in range(len(search_list)):
        if search_list[i] == num:
            ret.append(i)
    return ret




def binary_search(search_list, num):
    mid = len(search_list) //2

    if len(search_list) == 0:
        # print(1)
        # print(search_list, 'num:', num, 'mid:',mid)
        return 

    if type(search_list[0]) == int:
        # print(2)
        # print(search_list, 'num:', num, 'mid:',mid)
        tmp = search_list
        search_list =  [(i,idx) for idx,i in enumerate(tmp)]
    
    

    if len(search_list) == 1:
        # print(3)
        # print(search_list, num)
        if search_list[0][0] == num:
            ret.append(search_list[0][1])
            return search_list[0][1]
        else:
            return 

    elif num > search_list[mid][0]:
        # print(4)
        # print(search_list, 'num:', num, 'mid:',mid)
        return binary_search(search_list[:mid],num)
    
    elif num < search_list[mid][0]:
        # print(5)
        # print(search_list, 'num:', num, 'mid:',mid)
        
        return binary_search(search_list[mid+1:],num)
    
    else:
        return mid, binary_search(search_list[mid+1:],num), binary_search(search_list[:mid],num)
        
        # print(search_list, 'num:', num, 'mid:',mid)
