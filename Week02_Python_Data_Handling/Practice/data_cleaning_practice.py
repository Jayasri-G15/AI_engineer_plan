import pandas as pd

data = {
    "Name": ["John ", "Mary", "John ", "David", None],
    "Salary": ["50,000", "60000", "50,000", "55000", "70000"],
    "Date": ["2026-01-01", "2026-01-02", "2026-01-01", None, "2026-01-05"]
}

df = pd.DataFrame(data)

print(df.isnull().sum())
print(df.duplicated().sum())

df.drop_duplicates(inplace=True)

df["Name"] = df["Name"].astype("string").str.strip()

df["Salary"] = (
    df["Salary"]
    .str.replace(",", "", regex=False)
)

df["Salary"] = pd.to_numeric(
    df["Salary"],
    errors="coerce"
)

df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

print(df)
print(df.dtypes)