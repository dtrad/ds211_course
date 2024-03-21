
msg = "Nothing at the moment."

for counter in range(0, 10):
    if(counter % 2 != 0):
        msg = str(counter) + " is an odd number."
    else:
        msg = str(counter) + " is an even number."

    print(msg)    