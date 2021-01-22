
while True:
    y = int(input('연도를 입력하세요. (음수입력: 종료)'))
    if y < 0:
        print('감사합니다.')
        break 
    if y > 5000:
        print('0~5000 사이의 연도를 입력하세요')
        continue 

    if y%4==0 and y%100 !=0 or y%400==0:
        print(y,'년은 윤년입니다.')
    else:
        print(y,'년은 윤년이 아닙니다.')