# Recursive Binary Search

This program demonstrates a **recursive implementation** of the Binary Search algorithm in Python.

Binary Search is an efficient way to search a **sorted list** by repeatedly dividing the search interval in half. This version uses recursion instead of loops.

---

## 🔍 How the Algorithm Works

1. If the list is empty → return False  
2. Compute the middle index (`mid`)  
3. Compare the middle element with the target:
   - If equal → return True  
   - If the middle element is smaller → recursively search the right half  
   - If larger → recursively search the left half  

The recursion continues until the element is found or the sub-list becomes empty.

---

## 🧠 Function Overview

### `recursion_binary_search(lst, target)`

- **Parameters:**
  - `lst`: A sorted list of values
  - `target`: The value to search for
- **Returns:**  
  - `True` if the target is found  
  - `False` if not found

---

## 📈 Time Complexity

- **Best Case:** O(1)  
- **Worst Case:** O(log n)  
- **Average Case:** O(log n)

Recursive binary search provides the same efficiency as the iterative version but relies on repeated function calls.

---

## ▶️ Example Usage

```python
lst = [x for x in range(0, 51)]
num = int(input("Enter a number to search: "))

result = recursion_binary_search(lst, num)
print(result)
