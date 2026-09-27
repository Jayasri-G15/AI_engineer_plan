# NumPy

## 1. What is NumPy?

NumPy stands for **Numerical Python**.

It is a Python library mainly used for numerical computing and working with arrays.

NumPy is widely used in:

- Artificial Intelligence
- Machine Learning
- Data Science
- Scientific Computing
- Mathematical Operations

NumPy arrays are generally faster and more efficient for numerical operations than normal Python lists.

---

## 2. Importing NumPy

NumPy is normally imported using the alias `np`.

### Example

```python
import numpy as np
```

The alias allows us to write `np` instead of `numpy`.

---

## 3. Creating a NumPy Array

A NumPy array can be created using `np.array()`.

### Example

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)
```

Output:

```text
[10 20 30 40 50]
```

---

## 4. Mean

The mean is the average of all values.

The formula is:

**Mean = Sum of values / Number of values**

### Example

```python
numbers = np.array([10, 20, 30, 40, 50])

print(np.mean(numbers))
```

Output:

```text
30.0
```

---

## 5. Maximum

`np.max()` returns the highest value in an array.

### Example

```python
print(np.max(numbers))
```

Output:

```text
50
```

---

## 6. Minimum

`np.min()` returns the lowest value.

### Example

```python
print(np.min(numbers))
```

Output:

```text
10
```

---

## 7. Sum

`np.sum()` calculates the total of all values.

### Example

```python
print(np.sum(numbers))
```

Output:

```text
150
```

---

## 8. Two-Dimensional Arrays

NumPy can also store data in rows and columns.

### Example

```python
data = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])

print(data)
```

Output:

```text
[[10 20]
 [30 40]
 [50 60]]
```

This represents:

- 3 rows
- 2 columns

---

## 9. Shape

The `shape` property tells us the dimensions of an array.

### Example

```python
print(data.shape)
```

Output:

```text
(3, 2)
```

This means:

**3 rows × 2 columns**

---

## 10. NumPy Statistical Operations

NumPy provides many useful mathematical functions.

### Example

```python
marks = np.array([78, 85, 92, 67, 88])

print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Total:", np.sum(marks))
```

---

## Practice Task

Create marks for 10 students and calculate:

1. Average mark
2. Highest mark
3. Lowest mark
4. Total marks
5. Shape of the array