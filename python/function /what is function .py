#syntax: def name of function (parameters):
        #statement1
        # return 
       # var = function(value to parameter)
       # print(var)
"""
function: A function is a block of reusable code that performs a specific task.
Instead of writing the same code again and again, 
you write it once inside a function and use it whenever you want.
"""

# a = 4
# b = 2
# c = 1

# average = (a + b + c)/3.0
# print(average)

# a1 = 6
# b1 = 7
# c1 = 12

# average1 = (a1 + b1 + c1)/3
# print(average1)


def average(a, b, c):
    d = (a + b + c)/3.0
    # print(d)
    return d

o1 = average(3, 5, 1)
o2 = average(4, 2, 1)

print(o1)
print(o2)