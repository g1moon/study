#아나그램 : 알파벳의 나열 순서는 다르지만 -> 구성이 일치하면 -> 아나그램 
#두 단어의 딕셔너리를 만들고 포문 돌면서 -> 체크해서 더해나가자
#큐로 해결해보자
lst1 = list(input())
lst2 = list(input())

dic1, dic2 = {}, {}

for i in range(len(lst1)):
    try:
        dic1[lst1[i]] += 1
        dic2[lst2[i]] += 1
    except:
        dic1[lst1[i]] = 1
        dic2[lst2[i]] = 1
        
if dic1 ==dic2:
    print('YES')
else:
    print('NO')
print('-----------------------')