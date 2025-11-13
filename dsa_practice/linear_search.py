def liner__search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print('The value is fount at index', index)
    else:
        print('The value is not in lst')

lst = [x for x in range(11)]
num = int(input('enter a num: '))
result = liner__search(lst, num)

verify(result)

