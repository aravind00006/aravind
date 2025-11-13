# Binary Search Algorithm

This program demonstrates a standard implementation of the **Binary Search** algorithm in Python.

Binary Search is an efficient method for finding a target value within a **sorted list**.  
It works by repeatedly dividing the search range in half until the target is found or the range becomes empty.

---

## 🔍 How It Works

1. Define two pointers: `left` at the start and `right` at the end of the list.
2. Find the middle index: `(left + right) // 2`.
3. Compare the middle element with the target:
   - If equal → return the index.
   - If the target is greater → search the right half.
   - If the target is smaller → search the left half.
4. Repeat until the target is found or the range is invalid.

---

## 📈 Time Complexity

- **Best Case:** O(1)
- **Worst Case:** O(log n)
- **Average Case:** O(log n)

Binary Search is significantly faster than Linear Search for large datasets, but **only works on sorted lists**.

---

## ▶️ Example

**Input:**
