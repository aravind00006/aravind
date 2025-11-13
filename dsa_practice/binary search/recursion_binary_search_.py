def recursion_binary_search(lst, target):
    """
    This function uses recursion to perform a binary search and returns
    True if the target exists in the list, otherwise False.
    """
    if len(lst) == 0:
        return False
    
    mid = len(lst) // 2

    if lst[mid] == target:
        return True
    elif lst[mid] < target:
        return recursion_binary_search(lst[mid + 1:], target)
    else:
        return recursion_binary_search(lst[:mid], target)


# Example usage
lst = [x for x in range(0, 51)]
num = int(input("Enter a number to search: "))

result = recursion_binary_search(lst, num)
print(result)
