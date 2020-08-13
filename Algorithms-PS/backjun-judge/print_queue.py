#큐 맨 앞의 문서의 중요도 확인
#if 나머지 문서들 중 중요도  > 현재 문서 중요도 
#(1개라도) -> 문서를 인쇄하지 않고 -> queue의 맨 뒤로(s: pop(0) 하고 append())
#즉 중요도가 높은 순서 대로 출력                   

#가장 큰 인덱스 위치 찾고 -> 그 인덱스 어펜드 -> -1로 바꿔버려

in_list = [2,1,4,3,8]
queue = []
def f_max_idx(list_):
    max_idx = 0
    for i in range(len(list_)):
        if list_[max_idx] < list_[i]:
            max_idx = i
    return max_idx

while sum(in_list) != -len(in_list):
    max_idx = f_max_idx(in_list)
    print(max_idx)
    queue.append(max_idx)
    in_list[max_idx] = -1

queue
