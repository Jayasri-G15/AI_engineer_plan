# Data Cleaning with Pandas

## 1. What is Data Cleaning?

Data cleaning is the process of identifying and correcting problems in raw data before performing analysis.

Real-world datasets can contain:

- Missing values
- Duplicate records
- Incorrect data types
- Extra spaces
- Inconsistent text
- Invalid dates
- Incorrect numerical values

Clean data is important because incorrect data can produce incorrect analysis and business decisions.

---

## 2. Checking Missing Values

`isnull()` identifies missing values.

### Example

```python
df.isnull()
```

To count missing values in each column:

```python
df.isnull().sum()
```

This helps identify columns that need attention.

---

## 3. Checking Duplicate Records

`duplicated()` identifies duplicate rows.

### Example

```python
df.duplicated().sum()
```

This returns the number of duplicate rows.

---

## 4. Removing Duplicates

`drop_duplicates()` removes duplicate records.

### Example

```python
df.drop_duplicates(
    inplace=True
)
```

`inplace=True` applies the change directly to the DataFrame.

---

## 5. Removing Extra Spaces

Text data may contain unnecessary spaces.

### Example

```python
df["Name"] = df["Name"].str.strip()
```

For example:

```text
" John "
```

becomes:

```text
"John"
```

---

## 6. Standardizing Text

Text values may appear in different formats.

### Example

```python
df["Status"] = df["Status"].str.title()
```

This can convert values such as:

```text
active
ACTIVE
Active
```

into a consistent format:

```text
Active
```

---

## 7. Converting Dates

Dates should be converted into a proper datetime format for analysis.

### Example

```python
df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)
```

`errors="coerce"` converts invalid date values into `NaT`.

This allows us to identify invalid dates without stopping the program.

---

## 8. Converting Numerical Values

Sometimes numbers are stored as text.

### Example

```python
df["Salary"] = pd.to_numeric(
    df["Salary"],
    errors="coerce"
)
```

This converts valid values into numerical values.

Invalid values become `NaN`.

---

## 9. Cleaning Currency Values

Currency columns may contain symbols or commas.

For example:

```text
₹50,000
₹75,000
₹1,00,000
```

These values need to be cleaned before numerical calculations.

### Example

```python
df["Revenue"] = (
    df["Revenue"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.replace("₹", "", regex=False)
)

df["Revenue"] = pd.to_numeric(
    df["Revenue"],
    errors="coerce"
)
```

Now the values can be used for calculations.

---

## 10. Checking Data Types

The `dtypes` property displays the data type of every column.

### Example

```python
print(df.dtypes)
```

Common types include:

- `int64`
- `float64`
- `object`
- `string`
- `datetime64`

---

## 11. Why Data Cleaning is Important

Data cleaning ensures that:

- Calculations are accurate.
- Charts represent correct information.
- Statistical analysis is reliable.
- Machine learning models receive better data.
- Business decisions are based on trustworthy information.

### Basic Data Cleaning Workflow

```text
Raw Data
   ↓
Check Missing Values
   ↓
Check Duplicates
   ↓
Clean Text
   ↓
Convert Data Types
   ↓
Clean Dates
   ↓
Clean Numerical Values
   ↓
Clean Dataset
   ↓
Analysis
```