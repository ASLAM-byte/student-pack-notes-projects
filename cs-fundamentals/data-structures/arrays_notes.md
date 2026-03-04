# 📊 Arrays — Data Structures Notes

> "An array is a collection of elements stored in contiguous memory locations."

---

## 📖 Definition

An **array** is a linear data structure that stores a fixed-size, ordered collection of elements of the same type. Each element is identified by an **index** (starting at 0 in most languages).

Think of an array like a row of numbered boxes — each box holds one value, and you can access any box instantly if you know its number.

---

## ⚙️ How It Works

```
Index:   0     1     2     3     4
       +-----+-----+-----+-----+-----+
Array: |  10 |  20 |  30 |  40 |  50 |
       +-----+-----+-----+-----+-----+
```

- Elements are stored in **contiguous memory**
- Each element can be accessed using its **index** in O(1) time
- The size is usually **fixed** at creation (in static arrays)
- **Dynamic arrays** (like Python lists or JS arrays) can resize automatically

---

## ⏱️ Time Complexity

| Operation | Average Case | Worst Case | Notes |
|-----------|-------------|------------|-------|
| Access by index | O(1) | O(1) | Instant — just compute memory address |
| Search (unsorted) | O(n) | O(n) | Must check each element |
| Search (sorted) | O(log n) | O(log n) | Binary search possible |
| Insert at end | O(1) | O(n) | O(n) if resize needed |
| Insert at beginning/middle | O(n) | O(n) | Must shift elements |
| Delete from end | O(1) | O(1) | Just reduce size |
| Delete from beginning/middle | O(n) | O(n) | Must shift elements |

**Space Complexity:** O(n) — proportional to the number of elements.

---

## 💻 Code Examples

### Python

```python
# Creating an array (list in Python)
fruits = ["apple", "banana", "cherry"]

# Access by index
print(fruits[0])   # "apple"
print(fruits[-1])  # "cherry" (negative index: from end)

# Modify an element
fruits[1] = "mango"

# Add elements
fruits.append("grape")      # Add to end: O(1)
fruits.insert(1, "kiwi")    # Insert at index: O(n)

# Remove elements
fruits.pop()        # Remove from end: O(1)
fruits.pop(0)       # Remove from index: O(n)
fruits.remove("cherry")  # Remove by value: O(n)

# Iterate
for fruit in fruits:
    print(fruit)

# Slice
sub = fruits[1:3]   # Elements at index 1 and 2

# Length
print(len(fruits))
```

### JavaScript

```javascript
// Creating an array
const numbers = [10, 20, 30, 40, 50];

// Access by index
console.log(numbers[0]);    // 10
console.log(numbers.at(-1)); // 50 (last element)

// Add elements
numbers.push(60);       // Add to end: O(1)
numbers.unshift(0);     // Add to beginning: O(n)

// Remove elements
numbers.pop();          // Remove from end: O(1)
numbers.shift();        // Remove from beginning: O(n)

// Find elements
console.log(numbers.indexOf(30));  // 2
console.log(numbers.includes(20)); // true

// Array methods
const doubled = numbers.map(n => n * 2);
const evens = numbers.filter(n => n % 2 === 0);
const sum = numbers.reduce((acc, n) => acc + n, 0);

// Slice and splice
const sub = numbers.slice(1, 3);   // Copy elements [1, 3)
numbers.splice(2, 1);              // Remove 1 element at index 2
```

---

## 🌍 Use Cases

Arrays are best used when:

| Use Case | Why Arrays Work Well |
|----------|---------------------|
| Storing a list of items | Elements are ordered and accessible by index |
| Iteration / processing all elements | O(n) traversal is acceptable |
| Implementing other data structures | Stacks, queues, heaps often use arrays internally |
| Mathematical computations | NumPy arrays for fast vectorized operations |
| Fixed-size data | When you know the count of elements upfront |

Arrays are **not ideal** when:
- You frequently insert/delete from the middle → use a **Linked List**
- You need fast key-value lookup → use a **Hash Table / Dictionary**
- You need ordered insertions → use a **Tree** structure

---

## ✅ Key Takeaways

- Arrays offer **O(1) access** by index — their biggest advantage
- Inserting/deleting from the middle is **O(n)** — their main weakness
- In Python, `list` is a dynamic array; in JS, `Array` is dynamic
- For performance-critical code, use typed arrays (e.g., `numpy.ndarray`)
- Arrays are the foundation of many other data structures

---

*Last Updated: 2024-01-20*
