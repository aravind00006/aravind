def binary_search(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = lst[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return None


def verify(index):
    if index is not None:
        print("The value was found at index", index)
    else:
        print("The value is not in the list.")


lst = [x for x in range(0, 10)]
num = int(input("Enter a number to search: "))

result = binary_search(lst, num)
verify(result)
