# Data Visualization with Matplotlib

## 1. What is Matplotlib?

Matplotlib is a Python library used to create graphs and visualizations.

Visualization makes it easier to identify:

- Trends
- Comparisons
- Distributions
- Patterns
- Proportions
- Business performance

---

## 2. Importing Matplotlib

The `pyplot` module is normally imported as `plt`.

### Example

```python
import matplotlib.pyplot as plt
```

---

## 3. Bar Chart

A bar chart is used to compare different categories.

### Example

```python
products = ["Laptop", "Phone", "Tablet"]
sales = [50000, 75000, 30000]

plt.bar(products, sales)

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.show()
```

### Use

A bar chart can answer:

> Which product generated the highest sales?

---

## 4. Line Chart

A line chart is useful for showing changes and trends over time.

### Example

```python
months = ["Jan", "Feb", "Mar", "Apr", "May"]
revenue = [40000, 45000, 52000, 48000, 60000]

plt.plot(
    months,
    revenue,
    marker="o"
)

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.show()
```

### Use

A line chart can answer:

> Is revenue increasing or decreasing over time?

---

## 5. Histogram

A histogram shows the distribution of numerical values.

### Example

```python
values = [
    10, 12, 15, 15, 18,
    20, 22, 22, 25, 30
]

plt.hist(
    values,
    bins=5
)

plt.title("Value Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()
```

### Use

A histogram can answer:

> How are the numerical values distributed?

---

## 6. Pie Chart

A pie chart shows how different categories contribute to a whole.

### Example

```python
categories = ["IT", "HR", "Sales", "Finance"]
employees = [40, 20, 30, 10]

plt.pie(
    employees,
    labels=categories,
    autopct="%1.1f%%"
)

plt.title("Employees by Department")

plt.show()
```

### Use

A pie chart can answer:

> What percentage of employees belong to each department?

---

## 7. Chart Title

`plt.title()` adds a title to the chart.

### Example

```python
plt.title("Revenue by Product")
```

---

## 8. X-Axis Label

`plt.xlabel()` labels the horizontal axis.

### Example

```python
plt.xlabel("Product")
```

---

## 9. Y-Axis Label

`plt.ylabel()` labels the vertical axis.

### Example

```python
plt.ylabel("Revenue")
```

---

## 10. Showing the Chart

`plt.show()` displays the chart.

### Example

```python
plt.show()
```

---

## 11. Multiple Charts

Multiple charts can be displayed using subplots.

### Example

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].bar(
    ["A", "B", "C"],
    [10, 20, 15]
)

axes[0, 1].plot(
    [1, 2, 3],
    [10, 20, 15]
)

axes[1, 0].hist(
    [10, 12, 15, 20, 22]
)

axes[1, 1].pie(
    [40, 30, 30],
    labels=["A", "B", "C"]
)

plt.tight_layout()
plt.show()
```

---

## 12. Choosing the Right Chart

| Chart | Purpose |
|---|---|
| Bar Chart | Compare categories |
| Line Chart | Show trends |
| Histogram | Show numerical distribution |
| Pie Chart | Show proportions |

---

## 13. Visualization Workflow

```text
Analyze Data
    ↓
Choose Important Metric
    ↓
Choose Appropriate Chart
    ↓
Create Chart
    ↓
Add Title
    ↓
Add X/Y Labels
    ↓
Display Chart
    ↓
Interpret Result
```

---

## 14. Visualization in Business Analysis

For an organization, visualization can be used to show:

- Revenue by region
- Sales by product
- Monthly revenue
- Profit trends
- Customer segments
- Employee salary distribution
- Marketing performance
- Support ticket categories
- Project status

A good visualization allows management to understand important information quickly.