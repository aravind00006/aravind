# Linear Search Program

This program demonstrates a simple implementation of the **Linear Search** algorithm in Python.  
It checks each element in a list one by one to find a target value.

---

## 🔍 How the Program Works

### 1. `liner__search(lst, target)`
- Iterates through the list using index positions.
- Compares each element with the target.
- Returns the index if the target is found.
- Returns `None` if the target is not found.

### 2. `verify(index)`
- Prints a message confirming whether the target was found.
- If found, displays the index.
- If not found, tells the user the value isn't in the list.

---

## 🧠 Program Flow
1. Creates a list of numbers from 0 to 10.  
2. Takes a number as user input.  
3. Calls `liner__search()` to find the number.  
4. Uses `verify()` to show the result.

---

## ⏱️ Time Complexity
- **Best Case:** O(1) — target is at the first position  
- **Worst Case:** O(n) — target is at the end or not present  
- **Average Case:** O(n)  

Linear search is effective for small or unsorted lists.

---

## ▶️ Example Usage
**Input:**  
`enter a num: 5`

**Output:**  
`The value is fount at index 5`

---

## 📌 Notes
- The search uses a basic iterative approach.  
- Because the list is small (0–10), linear search is appropriate.  
- The function returns `None` instead of `-1`, which is a design choice but still valid.

---

## ✔️ Summary
This script is a clean and simple demonstration of how linear search works:  
loop through → compare values → return the index → show the result.
