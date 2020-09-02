# 구현 실전문제2 - 왕실의 나이트
'''
- 8 바이 8 
- 이동은 L자 형태로만 이동가능
- 메트릭스 밖으로 나갈 수 없음
    - 1. 수평으로 두칸이동, 수직으로 한칸 이동
        - 오른2, 위1
        - 오른2, 아래1
        - 왼2, 위1
        - 왼2, 아래1
    - 2. 수직으로 두칸이동, 수평으로 한칸 이동
        -오른1, 위2
        -오른1, 위2
        -왼1, 아래2
        -왼1, 아래2
'''
input_data = input()
xlst = [2, 2, -2, -2, 1, 1, -1, -1]
ylst = [-1, 1, -1, 1, 2, -2, +2, +2]

dic = {'a':1, 'b':2, 'c':3,'d':4, 'e':5, 'f':6, 'g':7, 'h':8}
y = dic[input_data[0]]
x = int(input_data[1])

for i in range(len(xlst)):
    new_x = x + xlst[i]
    new_y = y + ylst[i]
    if new_x >= 1 and new_x <=8 and new_y >=1 and new_y<=8:
        print(new_x, new_y)