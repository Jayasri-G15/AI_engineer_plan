# Python Practice

# 1. Variables

name = "John"
age = 25
salary = 50000.50
is_active = True

print("Name:", name)
print("Age:", age)
print("Salary:", salary)
print("Active:", is_active)


# 2. Data Types

print(type(name))
print(type(age))
print(type(salary))
print(type(is_active))


# 3. Lists

skills = ["Python", "AI", "Pandas"]

print(skills)
print(skills[0])

for skill in skills:
    print(skill)


# 4. Dictionaries

employee = {
    "name": "John",
    "age": 25,
    "department": "IT",
    "salary": 50000
}

print(employee)
print(employee["name"])
print(employee["department"])


# 5. Conditions

if salary > 50000:
    print("High Salary")
else:
    print("Normal Salary")


# 6. Loops

for number in range(1, 6):
    print(number)


# 7. Employee Information

employees = [
    {
        "name": "John",
        "age": 25,
        "department": "IT",
        "salary": 50000
    },
    {
        "name": "Mary",
        "age": 28,
        "department": "HR",
        "salary": 60000
    },
    {
        "name": "David",
        "age": 30,
        "department": "Sales",
        "salary": 55000
    },
    {
        "name": "Sarah",
        "age": 26,
        "department": "Finance",
        "salary": 52000
    },
    {
        "name": "Mike",
        "age": 32,
        "department": "IT",
        "salary": 70000
    }
]

for employee in employees:
    print(
        employee["name"],
        employee["age"],
        employee["department"],
        employee["salary"]
    )


# 8. Functions

def calculate_salary(salary, bonus):
    return salary + bonus


total_salary = calculate_salary(50000, 5000)

print("Total Salary:", total_salary)


# 9. Multiple Functions

def calculate_total(numbers):
    return sum(numbers)


def calculate_average(numbers):
    return sum(numbers) / len(numbers)


def find_max(numbers):
    return max(numbers)


def find_min(numbers):
    return min(numbers)


numbers = [10, 20, 30, 40, 50]

print("Total:", calculate_total(numbers))
print("Average:", calculate_average(numbers))
print("Maximum:", find_max(numbers))
print("Minimum:", find_min(numbers))


# 10. List Comprehension

squares = [x * x for x in numbers]

print("Squares:", squares)


# 11. List Comprehension with Condition

even_numbers = [
    x for x in numbers
    if x % 2 == 0
]

print("Even Numbers:", even_numbers)


# 12. Exception Handling

try:
    number = int(input("Enter a number: "))
    print("Number:", number)

except ValueError:
    print("Invalid number")

else:
    print("Number entered successfully")

finally:
    print("Program completed")