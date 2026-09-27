# Pandas

## 1. What is Pandas?

Pandas is a Python library used for working with structured and tabular data.

It is widely used in:

- Data Analysis
- Data Cleaning
- Data Science
- Machine Learning
- Business Intelligence

Pandas provides two important data structures:

- Series
- DataFrame

---

## 2. Importing Pandas

Pandas is normally imported using the alias `pd`.

### Example

```python
import pandas as pd
```

---

## 3. Creating a DataFrame

A DataFrame is a table containing rows and columns.

### Example

```python
data = {
    "Name": ["John", "Mary", "David"],
    "Age": [25, 30, 28],
    "Salary": [50000, 60000, 55000]
}

df = pd.DataFrame(data)

print(df)
```

The resulting DataFrame looks like:

```text
    Name  Age  Salary
0   John   25   50000
1   Mary   30   60000
2  David   28   55000
```

---

## 4. head()

`head()` displays the first rows of a DataFrame.

### Example

```python
df.head()
```

By default, it displays the first five rows.

We can specify the number of rows:

```python
df.head(2)
```

---

## 5. tail()

`tail()` displays the last rows.

### Example

```python
df.tail()
```

---

## 6. shape

`shape` returns the number of rows and columns.

### Example

```python
print(df.shape)
```

If the DataFrame has 3 rows and 3 columns:

```text
(3, 3)
```

---

## 7. info()

`info()` provides information about the DataFrame.

### Example

```python
df.info()
```

It provides:

- Number of rows
- Column names
- Data types
- Non-null values
- Memory usage

---

## 8. describe()

`describe()` provides statistical information about numerical columns.

### Example

```python
df.describe()
```

It can show:

- Count
- Mean
- Standard deviation
- Minimum
- Maximum
- Quartiles

---

## 9. Selecting a Column

A single column can be selected using its name.

### Example

```python
print(df["Salary"])
```

---

## 10. Selecting Multiple Columns

Multiple columns can be selected using a list.

### Example

```python
print(df[["Name", "Salary"]])
```

---

## 11. Filtering Rows

Filtering selects rows based on a condition.

### Example

```python
high_salary = df[df["Salary"] > 55000]

print(high_salary)
```

This returns employees whose salary is greater than `55000`.

---

## 12. Sorting Data

`sort_values()` sorts the DataFrame based on a column.

### Example

```python
df.sort_values(
    "Salary",
    ascending=False
)
```

`ascending=False` sorts from highest to lowest.

---

## 13. GroupBy

`groupby()` groups records based on a column.

### Example

```python
df.groupby("Name")["Salary"].mean()
```

It calculates the average salary for each name.

---

## 14. Aggregation

Aggregation allows multiple calculations to be performed together.

### Example

```python
df.groupby("Name").agg(
    AverageSalary=("Salary", "mean"),
    MaximumSalary=("Salary", "max")
)
```

---

## 15. value_counts()

`value_counts()` counts how many times each value appears.

### Example

```python
df["Name"].value_counts()
```

This is useful for understanding categories and frequencies.

---

## 16. Reading CSV Files

CSV files can be loaded using `read_csv()`.

### Example

```python
df = pd.read_csv("sales.csv")

print(df.head())
```

---

## 17. Reading Excel Files

Excel files can be loaded using `read_excel()`.

### Example

```python
df = pd.read_excel("data.xlsx")

print(df.head())
```

---

## 18. Reading Multiple Excel Sheets

An Excel workbook can contain multiple sheets.

### Example

```python
excel_file = pd.ExcelFile("data.xlsx")

print(excel_file.sheet_names)
```

A specific sheet can then be loaded:

```python
orders = pd.read_excel(
    "data.xlsx",
    sheet_name="Orders"
)
```

---

## Why Pandas is Important

Pandas provides the main tools required to:

- Load data
- Inspect data
- Clean data
- Filter data
- Sort data
- Group data
- Aggregate data
- Combine datasets
- Analyze business information