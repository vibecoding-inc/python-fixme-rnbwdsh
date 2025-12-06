from functools import reduce

# DATA SETUP
names = ["Alice", "Bob", "Charlie", "Dave", "Eve"]
grades = [85, 42, 60, 49, 90]

# 1. THE "ZIP" REINVENTION
# Creates a list of dicts using map/lambda, but casts to list immediately.
# Hard to read, unnecessary lambda usage.
data = list(map(lambda i: {'n': names[i], 'g': grades[i]}, range(names.__len__())))

# 2. THE FILTER MESS
# Defining a lambda to a variable name (PEP 8 violation).
# Using a magic number (50).
is_good = lambda x: True if x['g'] >= 50 else False
passed = list(filter(is_good, data))

# 3. THE CALCULATION (The worst part)
# Using reduce to sum integers is slower and less readable than sum().
# Also using a list comprehension INSIDE the reduce argument.
total_val = reduce(lambda a, b: a+b, [x['g'] for x in passed])

# 4. THE OUTPUT
# Calculating average inline with a ternary operator to avoid division by zero.
avg = total_val / passed.__len__() if passed.__len__() > 0 else 0

print("Processing complete.")
# 5. LIST COMPREHENSION FOR SIDE EFFECTS
# This creates a throwaway list just to print. A classic "Look, no loops!" mistake.
[print(f"Passed: {s['n']} ({s['g']})") for s in passed]

print("Count: " + str(passed.__len__()))
print("Average: " + str(avg))