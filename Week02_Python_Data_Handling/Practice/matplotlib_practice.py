#bar chart
import matplotlib.pyplot as plt

products = ["Laptop", "Phone", "Tablet", "Monitor"]
sales = [50000, 75000, 30000, 45000]

plt.bar(products, sales)
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

#line chart
months = ["Jan", "Feb", "Mar", "Apr", "May"]
revenue = [40000, 45000, 52000, 48000, 60000]

plt.plot(months, revenue, marker="o")
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()


#histogram
values = [10, 12, 15, 15, 18, 20, 22, 22, 25, 30]

plt.hist(values, bins=5)
plt.title("Value Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

#pie
categories = ["IT", "HR", "Sales", "Finance"]
employees = [40, 20, 30, 10]

plt.pie(
    employees,
    labels=categories,
    autopct="%1.1f%%"
)

plt.title("Employees by Department")
plt.show()