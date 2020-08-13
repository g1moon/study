def binary_search(a_list, item):
    if len(a_list) == 1 and item == a_list[0]:
        return True
    if len(a_list) == 1 and item != a_list[0]:
        return False
    if len(a_list) == 0:
        return False
    
    medium = len(a_list) // 2
    if item == a_list[medium]:
        return True
    else:
        if item > a_list[medium]:
            return binary_search(a_list[medium+1:], item)
        else:
            return binary_search(a_list[:medium], item)

def bubble_sort(a_list):
    for index in range(len(a_list) - 1):
        swap = False
        for index2 in range(len(a_list) - index - 1):
            if a_list[index2] > a_list[index2 + 1]:
                a_list[index2], a_list[index2 + 1] = a_list[index2 + 1], a_list[index2]
                swap = True
        
        if swap == False:
            break
    return a_list

def selection_sort(a_list):
    for stand in range(len(a_list) - 1):
        lowest = stand
        for index in range(stand + 1, len(a_list)):
            if a_list[lowest] > a_list[index]:
                lowest = index
        a_list[lowest], a_list[stand] = a_list[stand], a_list[lowest]
    return a_list

def insertion_sort(a_list):
    for index in range(len(a_list) - 1):
        for index2 in range(index + 1, 0, -1):
            if a_list[index2] < a_list[index2 - 1]:
                a_list[index2], a_list[index2 - 1] = a_list[index2 - 1], a_list[index2]
            else:
                break
    return a_list

# We start here!
count = int(input("Enter the number of numbers: ")) 

num_list = []
for i in range(0, count):
    number = int(input("Enter the number: "))
    num_list.append(number) 

print("The number list is", num_list)
while True:
    stype = input("Enter the types of sort: ")
    if stype == 'bubble':
        num_list = bubble_sort(num_list)
        break 
        # print(buuble_sort(num_list))

    elif stype == 'selection':
        num_list = selection_sort(num_list) 
        break
        # print(selection_sort(num_list))

    elif stype == 'insertion':
        num_list = insertion_sort(num_list) 
        break
        # print(insertion_sort(num_list))

    else:
        continue

print("The sorted number list is", num_list)

target = int(input("Enter the target number to find: ")) 
result = binary_search(num_list, target)
if result == True:
    print("We found!") 
else:
    print("We cannot found!")
