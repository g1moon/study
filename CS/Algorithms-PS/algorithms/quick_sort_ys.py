#퀵소트 
#left_mark right_mark

#1.select the pivot value
#2.find the split point(최종적으로 소팅된 피벗벨류가 들어가야하는것이고)
#이걸 partition process라고 한다.

#left마크는 피벗벨류 다음, rifht는 맨뒤 
#left마크는 피벗벨류와 비교해 작으면 패스 -> 피벗벨류보다 "크면" -> 멈춰
#라이트마크는 -> 크면 넘어가 ->피벗벨류랑 비교해서 "작으면" 멈춰 -> 
#두개의 마크가 멈추면 이 두개의 위치를 exchange 
#그리고 left마크 그 위치에서 시작 
#이러면서 마크 두개가 크로스되거나 넘어갔을때 -> 이동을 멈춰준다.

#이때 라이트마크가 스플릿 포인트 

# def quick_sort(lst):
#     #리스트를 입력으로 받아서 맨 앞과 맨 뒤 인덱스를를 찾아주는 
#     quick_sort_helper(lst, 0, len(lst)-1):
    
# def quick_sort_helper(lst, first, last):
#     #작을 경우에만 파티션닝해
#     if first < last:
#         split_point = partition(lst, forst, last)
        
#         quick_sort 

# #리스트의 first인덱스와 last인덱스를 받고 left_mark와 right_mark를 잡아줌
# def partition(lst, first, last):
#     pivot_value = lst[first]
#     left_mark = first + 1
#     right_mark = last
#     done = False        
    
#     while not done:
#         #이 두조건이 맞으면 left_mark를 increase
#         while (left_mark <= right_mark) and \
#             lst[left_mark]  <= pivot_value:
#                 left_mark = left_mark + 1
#         #항상 레프트 마크보다 크거나 같아야하고, 피벗테이블보다 크거나 같아야함 
#         while left_mark <= right_mark and \
#             lst[right_mark] >= pivot_value:
#                 right_mark = right_mark - 1    
#         #만약 left_mark가 더 크면 -> 반복문 이제 안켜짐
#         #else:아니면 left_mark와 right_mark값을 바꿔줌 
#         if right_mark < left_mark:
#             done = True
#         else:
#             tmp = lst[left_mark]
#             lst[left_mark] = lst[right_mark]
#             lst[right_mark] = tmp
            
#     #lst[first]와 right_mark값을 바꿔줌
#     tmp = lst[first]
#     lst[first] = lst[right_mark]
#     lst[right_mark] = tmp 
    
#     return right_mark
    
###############################################3
def quick_sort(lst):
    quick_sort_helper(lst, 0, len(lst)-1)
    
def quick_sort_helper(lst, first, last):
    if first < last:
        split_point = partition(lst, first, last)  #return으로 right_mark
        #계속해서 first와 last는 갱신이 될 것임
        quick_sort_helper(lst, first, split_point-1)
        quick_sort_helper(lst, split_point+1, last)
    
def partition(lst, first, last):
    pivot_value = lst[first]
    left_mark = first + 1
    right_mark = last 
    done = False
    
    while not done:
        #left_mark를 right마크를 움직여주고 
        #멈췃을때 .. 두 점이 크로스되어있으면 종료
        while left_mark <= right_mark and \
            lst[left_mark] <= pivot_value:
                left_mark += 1
                
        while left_mark <= right_mark and \
            lst[right_mark] >= pivot_value:
                right_mark -=1
        #위에서 움직였고 그게 끝났을 때 크로스되어있으면
        if right_mark < left_mark:
            done = True
        else:
            lst[left_mark], lst[right_mark] = lst[right_mark], lst[left_mark]
    
    #그리고 크로스돼서 다 끝났으면 -> 레프트랑 라이트는 교환안해주고
    #라이트마크와 피벗을 바꿔죠(first와 라이트)
    #바꿔주고 끝낼거야 그리고 right_marks는 스플릿 포인트
    lst[first], lst[right_mark] = lst[right_mark], lst[first]
    
    return right_mark

lst = [2,4,1,5,6,7,8,1,2,22,12,2]
quick_sort(lst)
print(lst)