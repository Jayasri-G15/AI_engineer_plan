import pandas as pd

file_path = "Organization_Business_Data.xlsx"

print(pd.ExcelFile(file_path).sheet_names)

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

print(orders.head())
print(customers.head())
print(products.head())

print(orders.shape)
print(orders.dtypes)

print(orders.isnull().sum())

orders["TotalAmount_INR"] = pd.to_numeric(
    orders["TotalAmount_INR"],
    errors="coerce"
)

print(
    orders.groupby("Region")["TotalAmount_INR"].sum()
)

result = orders.merge(
    customers,
    on="CustomerID",
    how="left"
)

result = result.merge(
    products,
    on="ProductID",
    how="left"
)

print(result.head())