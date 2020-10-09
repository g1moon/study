'''
- v는 뱀파이어 넘버
- 만약 이븐넘 n 을 갖고, 네츄럴 x,y 로 펙터 된다고 n/2digit을 갖는
- 인티저 x와 y는 cannot both have trailing zeros
- v는 x와 y로 부터 정확하게 모든 디짓을 포함해야해
- x,y를 뱀파이어 넘버(v)의 fangs라고 한다.

- v = x * b 
- x와 y에 등장하는 숫자는 v와 같아야한다. 
- x와 y는 짝수여야 한다.
- x와 y의 길이는 같아야 한다 (string으로 변환후 ck)

- 반복문으로 x를 i로 잡고 y = v // x
- if x * y == v -> return
- x와 y의 길이가 같은지 체크 
- x와 y의 맨 마지막이 '0'이면 -> return 
- 
'''

v = int(input())
for i in range(1, (v//2)+1):
    x = i 
    y = v // x
    
    #ck1
    if x * y != v:
        continue
    #ck2
    if len(str(x)) != len(str(y)):
        continue 
    #ck3
    if str(x)[-2:] == '00' or str(y)[-2:] == '00':
        continue 
    
    contain = True 
    for i in str(x):
        if i not in str(v):
            contain = False
            break 
        
    for j in str(y):
        if j not in str(v):
            contain = False
            break 
        
    if contain:
        print(v, ' is a vampire number.')
        break 
else:
      print(v, ' is not a vampire number.')