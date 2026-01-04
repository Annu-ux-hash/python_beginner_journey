def add(a, b, plus=0):
    x = a + b + plus
    return x


c = add(3, 5, 2)
print(c)

c1 = add(b=5, a=3)

# types : positional = Values are passed in order. Position matters.
def add(a, b):
    print(a + b)

add(2, 3)
add(3, 3)
#deafault = A function parameter already has a default value.
#If you don’t pass a value, Python uses the default.
def greet(name="User"):
    print("Hello", name)

greet()
greet("Anand")
#keyword argument. =You pass values using parameter names, so order does not matter.
def student(name, age):
    print(name, age)

student(age=20, name="Anand")