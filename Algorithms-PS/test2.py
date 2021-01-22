dic = {}

while True:
    name = input('[입력] 이름을 입력하세요(r:검색, q종료):')
    if name == 'q':
        break 
    
    if name == 'r':
        fname = input('[입력]찾아낼 이름을 입력하세요(r:검색, q종료):')
        if fname not in dic.keys():
            print('해당 사람이 없습니다.')
        if fname in dic.keys():
            print(dic[fname])
    else:
        num = input('전화번호를 입력하세요: ')
        dic[name] = num 