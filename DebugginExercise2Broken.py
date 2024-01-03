# Your program causes a simulated population of bacteria to grow in size. Every minute, the population size should be multiplied by 2x the number of the minute.
# For example, during minute 5, the population size should be multiplied by 10. Accept the initial population size from the user and print the simulated population
# size for each of the next 10 minutes.

initial_size = int(input("Enter the initial population size: "))
growing_size = initial_size


print("Bacteria population growth with initial size of ", initial_size, ":")

for i in range (10):
    growing_size = growing_size * i * 2
    print("Size at minute ", i, ": ", growing_size)
