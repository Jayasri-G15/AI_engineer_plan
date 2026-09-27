# Data Analysis with Pandas

## 1. What is Data Analysis?

Data analysis is the process of examining, transforming, and summarizing data to discover useful information and patterns.

In business analysis, data analysis helps answer questions such as:

- How much revenue was generated?
- Which product performed best?
- Which region generated the most sales?
- How many customers are there?
- Which month performed best?
- Which department has the most employees?

---

## 2. Selecting Data

Specific columns can be selected from a DataFrame.

### Example

```python
df[["Name", "Department", "Salary"]]
```

This allows us to focus only on the required information.

---

## 3. Filtering Data

Filtering selects rows that satisfy a condition.

### Example

```python
high_salary = df[
    df["Salary"] > 50000
]

print(high_salary)
```

This returns records where salary is greater than `50000`.

---

## 4. Sorting Data

Sorting helps identify the highest or lowest values.

### Example

```python
df.sort_values(
    "Salary",
    ascending=False
)
```

This places the highest salary first.

---

## 5. GroupBy

`groupby()` divides data into groups based on a category.

### Example

```python
df.groupby("Department")["Salary"].mean()
```

This calculates the average salary for each department.

---

## 6. Sum

`sum()` calculates the total.

### Example

```python
total_sales = df["Revenue"].sum()

print(total_sales)
```

---

## 7. Mean

`mean()` calculates the average.

### Example

```python
average_sales = df["Revenue"].mean()

print(average_sales)
```

---

## 8. Count

`count()` counts available values.

### Example

```python
df["OrderID"].count()
```

For unique orders:

```python
df["OrderID"].nunique()
```

---

## 9. Multiple Aggregations

Multiple calculations can be performed using `agg()`.

### Example

```python
summary = df.groupby("Region").agg(
    TotalRevenue=("Revenue", "sum"),
    AverageRevenue=("Revenue", "mean"),
    TotalOrders=("OrderID", "count")
)

print(summary)
```

This creates a summarized business report by region.

---

## 10. Merge

Real-world organizations usually store different types of information in different tables.

For example:

```text
Orders
Customers
Products
Employees
Departments
```

These datasets can be connected using common ID columns.

`merge()` combines related DataFrames.

### Example

```python
result = orders.merge(
    customers,
    on="CustomerID",
    how="left"
)
```

Here:

- `orders` is the main DataFrame.
- `customers` contains customer information.
- `CustomerID` is the common key.
- `how="left"` keeps all records from Orders.

---

## 11. Types of Merge

Common merge types are:

### Inner Merge

Returns matching records from both datasets.

```python
df1.merge(
    df2,
    on="ID",
    how="inner"
)
```

### Left Merge

Keeps all records from the left DataFrame.

```python
df1.merge(
    df2,
    on="ID",
    how="left"
)
```

### Right Merge

Keeps all records from the right DataFrame.

```python
df1.merge(
    df2,
    on="ID",
    how="right"
)
```

### Outer Merge

Keeps records from both DataFrames.

```python
df1.merge(
    df2,
    on="ID",
    how="outer"
)
```

---

## 12. Key Performance Indicators

KPIs are important metrics used to measure business performance.

### Total Revenue

```python
total_revenue = df["Revenue"].sum()
```

### Total Orders

```python
total_orders = df["OrderID"].nunique()
```

### Average Order Value

```python
average_order_value = (
    total_revenue / total_orders
)
```

### Best Product

```python
best_product = (
    df.groupby("Product")["Revenue"]
    .sum()
    .idxmax()
)
```

### Best Region

```python
best_region = (
    df.groupby("Region")["Revenue"]
    .sum()
    .idxmax()
)
```

---

## 13. Business Analysis Workflow

A typical analysis workflow is:

```text
Load Data
    ↓
Inspect Data
    ↓
Clean Data
    ↓
Select Required Data
    ↓
Filter Records
    ↓
Group Data
    ↓
Aggregate Values
    ↓
Merge Related Data
    ↓
Calculate KPIs
    ↓
Create Visualizations
    ↓
Generate Insights
```

The purpose of this workflow is to convert raw data into useful business information.