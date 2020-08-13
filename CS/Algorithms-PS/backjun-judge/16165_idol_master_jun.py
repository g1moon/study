#16165번: 걸그룹 마스터 준석이
#n = 입력받을 걸그룹의 수 , #m = 맞춰야하는 문제수 

input_data = list(map(int, input().split()))
n, m = input_data[0], input_data[1]

#팀이름
#걸그룹인원수
#멤머들이름이 차례대로(100글자이내 소문자)
#하나의 걸그룹이나 서로 다른 두 걸구룹이름에 같은 멤버 없음
def find_group(dic,mem):
    for k in dic.keys():
        if mem in dic[k]:
            return k

dic = {} #정보를 저장할 딕셔너리
#3번
for _ in range(n):
    team_name = input()
    mem_num = int(input())
    dic[team_name] = []
    for i in range(mem_num):
        dic[team_name].append(input())
    dic[team_name].sort()
        
#dic만들기 끝
#퀴즈
for _ in range(m):
    q = input() #맴버나, 그룹
    is_mem = int(input())
    
    if is_mem == 1:
        #그 멤버의 그룹을 맞추기
        print(find_group(dic, q))
    elif is_mem == 0: #그룹이라면
        for i in dic[q]:
            # pass
            print(i)
            


