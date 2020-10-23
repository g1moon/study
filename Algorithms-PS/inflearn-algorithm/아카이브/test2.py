import random 
l = [0,0,0,0,0,0,0,0,0,0,0]
for i in range(1200):
    a = random.randint(1,6)
    b = random.randint(1,6)
    total = a + b
    l[total-2] += 1

for i in range(11):
    print('합',i+2, ':', l[i] )