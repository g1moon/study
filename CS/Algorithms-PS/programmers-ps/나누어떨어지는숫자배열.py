
def f_min_idx(in_list):
    min_idx = 0
    for i in range(len(in_list)):
        if in_list[min_idx] > in_list[i]:
            min_idx = i

    return min_idx

# print(f_asort([12,3,0,3,4]))
    
def f_asort(in_list):
    sorted_list = []
    while in_list:
        # print(f_min_idx(in_list), in_list[f_min_idx], in_list)
        min_idx = f_min_idx(in_list)
        item = in_list.pop(min_idx)
        sorted_list.append(item)
    return sorted_list



def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor ==0:
            answer.append(arr[i])
    
    answer = f_asort(answer)

    if len(answer) == 0:
        return [-1]



    return answer

