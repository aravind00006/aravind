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

def binary_search(lst, target):
    first = 0
    last = len(lst) - 1

    while first <= last:
        middle = (first + last) //2

        if lst[middle] == target:
            return middle
        elif lst[middle] < target:
            first = middle + 1
        else:
            last = middle - 1
    return None


res = binary_search(lst, num)
verify(res)