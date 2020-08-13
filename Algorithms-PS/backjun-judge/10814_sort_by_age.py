n = int(input())
array = []

for _ in range(n):
    input_data = input().split(' ')
    array.append((int(input_data[0]), input_data[1]))

# array = [(21, 'Junkyu'), (21, 'Dohyun'), (20, 'Sunyoung'), (21, 'ss')]

array = sorted(array, key=lambda x: x[0])
array.sort()
array
