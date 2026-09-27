import pandas as pd

data = {
    "Name": ["John", "Mary", "David", "Sarah", "Mike"],
    "Age": [25, 28, 30, 26, 32],
    "Department": ["IT", "HR", "IT", "Sales", "Finance"],
    "Salary": [50000, 60000, 55000, 52000, 70000]
}

df = pd.DataFrame(data)

print(df)
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

print(df[["Name", "Salary"]])

print(df[df["Salary"] > 55000])

print(df.groupby("Department")["Salary"].mean())

print(df.sort_values("Salary", ascending=False))