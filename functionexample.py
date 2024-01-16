def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

# Using the functions
result_add = add(5, 3)
result_subtract = subtract(7, 2)
result_multiply = multiply(4, 6)
result_divide = divide(8, 4)

# Print results
print("Using Functions:")
print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)
