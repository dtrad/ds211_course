class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero."

# Creating an instance of the Calculator class
calc_instance = Calculator()

# Using the class methods
result_add_class = calc_instance.add(5, 3)
result_subtract_class = calc_instance.subtract(7, 2)
result_multiply_class = calc_instance.multiply(4, 6)
result_divide_class = calc_instance.divide(8, 4)

# Print results
print("\nUsing Class:")
print("Addition:", result_add_class)
print("Subtraction:", result_subtract_class)
print("Multiplication:", result_multiply_class)
print("Division:", result_divide_class)
