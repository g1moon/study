input_str = input()
l = []
for i in input_str:
    l.append(int(i))

l.sort(reverse=True)

for i in l:
    print(i, end = '')
