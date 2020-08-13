#17269번 이름 궁합 테스트 
#https://www.acmicpc.net/status?user_id=yangeb0&problem_id=17269&from_mine=1

input_data = list(map(int, input().split()))
l1, l2  = input_data[0], input_data[1]
input_data = list(map(str, input().split()))
n1, n2 = input_data[0], input_data[1]

name1 = (n1,l1)
name2 = (n2,l2)

alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]

dic = {}
for i in range(len(alp)):
    dic[alp[i]] = num[i]

isSame = False
if name1[1] > name2[1]:
    shorter = name2
    longer = name1
elif name1[1] < name2[1]:
    shorter = name1
    longer = name2
else:
    isSame = True

#작은 거 만큼 돌아주고
com = ''

if isSame:
    for i in range(name1[1]):
        com += name1[0][i]
        com = com + name2[0][i]

else:
    for i in range(shorter[1]):
        com = com + name1[0][i]
        com = com + name2[0][i]
    com += longer[0][shorter[1]:]
#
arr = [ dic[i.lower()] for i in com]



i = 0 
while True :
    new_arr = []
    if len(arr) == 2:
        break
    
    for i in range(0, len(arr)-1):
        item = arr[i] + arr[i+1]
        if item >= 10:
            new_arr.append(item % 10)
        else:
            new_arr.append(item)
    arr = new_arr

print(f'{(arr[0] % 10) * 10 + arr[1] % 10}%') # 정답