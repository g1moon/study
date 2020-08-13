class userManage:
    def __init__(self) :
       self.class_lst = []
        
    def print_info(self) :
        for i in range(len(self.class_lst)):
            a = self.class_lst[i]
            print("이름은 %s, 전화번호는 %s, 성별은 %s입니다" % (a[0], a[1], a[2]))
        
    def append_user(self,lst):
        self.class_lst.append(lst)

##
user_manage = userManage()
while True:
    name = input("이름을 입력하세요: ")
    if name == "그만" :
        break
    num = input("전화번호를 입력하세요: ")
    sex = input("성별을 입력하세요: ") 
    if (sex != 'male')  and (sex != 'female'):
        sex = 'unknown'
    
    user_lst = [name, num, sex]
    user_manage.append_user(user_lst)
    user_manage.print_info()
    print('\n')