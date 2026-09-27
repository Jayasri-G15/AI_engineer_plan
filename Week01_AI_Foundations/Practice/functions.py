# ==========================================
# Python Functions Practice
# ==========================================

# 1. Simple function

def greet():
    print("Hello, AI Engineer!")


greet()


# 2. Function with a parameter

def greet_person(name):
    print("Hello", name)


greet_person("Jayasri")
greet_person("John")


# 3. Function with two parameters

def add_numbers(a, b):
    print("Sum:", a + b)


add_numbers(10, 20)


# 4. Function returning a value

def multiply(a, b):
    return a * b


result = multiply(5, 4)

print("Multiplication result:", result)


# 5. Function with default parameter

def welcome(name="Student"):
    print("Welcome", name)


welcome()
welcome("Jayasri")


# 6. Function to check even number

def is_even(number):

    if number % 2 == 0:
        return True
    else:
        return False


print("\nIs 10 even?", is_even(10))
print("Is 7 even?", is_even(7))