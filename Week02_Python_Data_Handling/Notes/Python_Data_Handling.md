# Python Fundamentals for AI and Data Handling

## 1. Variables

Variables are used to store information in Python.

A variable can store different types of values such as numbers, text, or Boolean values.

### Example

```python
name = "John"
age = 25
salary = 50000
```

Here:

- `name` stores a person's name.
- `age` stores an integer.
- `salary` stores a salary value.

We can print the values using:

```python
print(name)
print(age)
print(salary)
```

---

## 2. Data Types

Python has different data types for storing different kinds of information.

Common Python data types include:

- **int** – Integer numbers
- **float** – Decimal numbers
- **str** – Text or strings
- **bool** – True or False values
- **list** – Collection of multiple values
- **tuple** – Ordered and immutable collection
- **dictionary** – Data stored as key-value pairs
- **set** – Unordered collection of unique values

### Example

```python
age = 25
salary = 50000.50
name = "John"
is_active = True

print(age)
print(salary)
print(name)
print(is_active)
```

---

## 3. Lists

Lists are used to store multiple values in a single variable.

Lists are ordered and can contain multiple items.

### Example

```python
skills = ["Python", "AI", "Pandas"]

print(skills)
print(skills[0])
```

Here:

- `skills` is the list.
- `"Python"`, `"AI"`, and `"Pandas"` are the elements.
- `skills[0]` accesses the first element.
- Python list indexing starts from `0`.

---

## 4. Dictionaries

Dictionaries store data using key-value pairs.

Each value can be accessed using its corresponding key.

### Example

```python
employee = {
    "name": "John",
    "age": 25,
    "salary": 50000
}

print(employee["name"])
```

Here:

- `"name"`, `"age"`, and `"salary"` are keys.
- `"John"`, `25`, and `50000` are their corresponding values.
- `employee["name"]` retrieves the value associated with the `"name"` key.

---

## 5. Conditions

Conditions are used for decision making in Python.

The `if` statement checks a condition. If the condition is true, its block is executed. Otherwise, the `else` block is executed.

### Example

```python
salary = 60000

if salary > 50000:
    print("High Salary")
else:
    print("Normal Salary")
```

Since `60000 > 50000`, the output is:

```text
High Salary
```

---

## 6. Loops

Loops are used to repeat an operation multiple times.

A `for` loop is commonly used to iterate through items in a list.

### Example

```python
skills = ["Python", "AI", "Pandas"]

for skill in skills:
    print(skill)
```

Output:

```text
Python
AI
Pandas
```

The loop takes each item from the list one by one.

---

## 7. Functions

Functions are reusable blocks of code that perform a specific task.

They help organize code and avoid repeating the same logic.

### Example

```python
def calculate_salary(salary, bonus):
    return salary + bonus

print(calculate_salary(50000, 5000))
```

Here:

- `calculate_salary` is the function name.
- `salary` and `bonus` are parameters.
- `return` sends the result back.
- `50000` and `5000` are arguments.

Output:

```text
55000
```

---

## 8. List Comprehension

List comprehension provides a short way to create a new list.

### Example

```python
numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

The expression:

```python
[x * x for x in numbers]
```

takes every number from `numbers`, calculates its square, and creates a new list.

---

## 9. Exception Handling

Exception handling is used to handle errors that may occur while a program is running.

Python provides four important keywords:

- `try` – Contains code that may produce an error.
- `except` – Handles the error.
- `else` – Runs when no error occurs.
- `finally` – Runs whether an error occurs or not.

### Example

```python
try:
    number = int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Invalid number")

else:
    print("Number entered successfully")

finally:
    print("Program completed")
```

### Why Exception Handling is Important

Exception handling prevents unexpected errors from immediately stopping a program.

It allows the program to handle errors in a controlled way.