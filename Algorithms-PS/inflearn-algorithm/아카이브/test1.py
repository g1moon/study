while True:
    dan = int(input('출력 단을 입력하세요.(0:종료)')) 
    if dan == 0:
        print('감사합니다.')
        break 
        
    if dan < 1 or dan > 9:
        print('1~9사이의 숫자를 입력하세요.')
        continue


    for i in range(1, 10):
        print(dan, 'X', i, '=', i*dan  )