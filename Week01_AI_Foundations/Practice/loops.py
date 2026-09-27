# ==========================================
# Python Loops Practice
# ==========================================

# 1. For loop with a list

languages = ["Python", "Java", "SQL"]

print("Programming Languages:")

for language in languages:
    print(language)


# 2. Using range()

print("\nNumbers from 1 to 5:")

for number in range(1, 6):
    print(number)


# 3. Calculating squares

print("\nSquares:")

for number in range(1, 6):
    print(number, "squared =", number ** 2)


# 4. While loop

print("\nWhile Loop:")

count = 1

while count <= 5:
    print(count)
    count = count + 1


# 5. Using if inside a loop

print("\nEven Numbers:")

for number in range(1, 11):

    if number % 2 == 0:
        print(number)


# 6. Continue

print("\nUsing continue:")

for number in range(1, 6):

    if number == 3:
        continue

    print(number)


# 7. Break

print("\nUsing break:")

for number in range(1, 10):

    if number == 5:
        break

    print(number)