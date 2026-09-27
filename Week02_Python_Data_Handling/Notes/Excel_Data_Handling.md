# Excel Data Handling with Pandas

## 1. Reading an Excel Workbook

Pandas can read Excel files using `read_excel()`.

### Example

```python
import pandas as pd

file_path = "Organization_Business_Data.xlsx"

df = pd.read_excel(
    file_path,
    sheet_name="Orders"
)

print(df.head())
```

---

## 2. Viewing Sheet Names

An Excel workbook can contain multiple sheets.

### Example

```python
excel_file = pd.ExcelFile(file_path)

print(excel_file.sheet_names)
```

This helps us understand the structure of the workbook before analysis.

---

## 3. Loading Multiple Sheets

Different sheets can be loaded into different DataFrames.

### Example

```python
orders = pd.read_excel(
    file_path,
    sheet_name="Orders"
)

customers = pd.read_excel(
    file_path,
    sheet_name="Customers"
)

products = pd.read_excel(
    file_path,
    sheet_name="Products"
)
```

---

## 4. Relationship Between Sheets

Different sheets can be connected using common ID columns.

For example:

```text
Customers
    |
    | CustomerID
    ↓
Orders
    |
    | ProductID
    ↓
Products
```

The IDs act as keys that connect related information.

---

## 5. Merging Sheets

### Example

```python
orders_analysis = orders.merge(
    customers,
    on="CustomerID",
    how="left"
)
```

Another sheet can then be added:

```python
orders_analysis = orders_analysis.merge(
    products,
    on="ProductID",
    how="left"
)
```

---

## 6. Why Multiple Sheets are Useful

Organizations normally store different business areas separately.

For example:

- Employees
- Departments
- Customers
- Products
- Orders
- Finance
- Marketing
- Attendance
- Support
- Projects

Keeping them separately makes the data organized.

Pandas can combine these datasets when analysis requires information from multiple areas.

---

## 7. Excel Analysis Workflow

```text
Excel Workbook
      ↓
Identify Sheets
      ↓
Load Sheets using Pandas
      ↓
Inspect Data
      ↓
Clean Data
      ↓
Identify Relationships
      ↓
Merge Related Data
      ↓
Analyze
      ↓
Calculate KPIs
      ↓
Create Charts
      ↓
Build Dashboard
```

---

## 8. Business Purpose

The final objective is not just to display data.

The objective is to convert organizational data into meaningful information that allows management to understand:

- Revenue performance
- Sales performance
- Customer performance
- Product performance
- Employee information
- Financial performance
- Marketing performance
- Support performance
- Project performance

This allows the owner or management team to make better business decisions based on data.