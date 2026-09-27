# ==========================================
# Python Lists Practice
# ==========================================

# 1. Creating a list
languages = ["Python", "Java", "C++", "JavaScript"]

print("Languages:", languages)

# 2. Accessing items
print("\nFirst language:", languages[0])
print("Second language:", languages[1])

# 3. Last item
print("Last language:", languages[-1])

# 4. Number of items
print("Number of languages:", len(languages))

# 5. Adding an item
languages.append("SQL")
print("\nAfter adding SQL:", languages)

# 6. Removing an item
languages.remove("C++")
print("After removing C++:", languages)

# 7. Changing an item
languages[0] = "Python 3"
print("After changing first item:", languages)

# 8. Checking whether an item exists
if "Python 3" in languages:
    print("Python 3 is in the list")

# 9. Slicing
print("\nFirst two languages:", languages[:2])

# 10. Looping through a list
print("\nProgramming Languages:")

for language in languages:
    print(language)