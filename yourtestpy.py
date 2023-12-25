# write your test code here
# import your module
# create a function to sort a list input a to convert it into a sorted list b using qsort

def qsort(a):
    if len(a) <= 1:
        return a
    else:
        pivot = a[0]
        return qsort([x for x in a[1:] if x < pivot]) + [pivot] + qsort([x for x in a[1:] if x >= pivot])

# test your function
print(qsort([3, 2, 1]))
    