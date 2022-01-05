# A function can be assigned to a variable
""" def greet(name):
    print(f"Hello, {name}")

welcome = greet
welcome("Sagar") """

# A function can be nested within another function
""" def outer():
    def inner():
        print("I am inner function")
    inner()
    
outer() """

# Since a function can be nested inside another function it can also be returned
""" def outer():
    def inner():
        print("I am inner function")
    return inner
    
fun = outer()
fun() """

#  function can be passed to another function as an argument.
""" def dosomething(whattodo):
    whattodo()
    print("...and then you can go!")

def something():
    print('Something doing')
    
dosomething(something) """

# ----------------------------------------------------------------------------

# Syntax of basic decorator
""" def decorator(func):
    def wrapper():
        print("Something is being done before")
        func()
        print("Something is being done before")
    return wrapper

@decorator
def myfunc():
    print("This is my func") """
    

# Example
def isnumber(func):
    def wrapper(n):
        if n.isnumeric():
            func(int(n))
        else:
            print(f"{n} is NaN")
    return wrapper

@isnumber
def isprime(n):
    count = 0
    for i in range(1,n+1):
        if n%i==0:
            count = count + 1
    if count==2:
        print(f"{n} is prime")
    else:
        print(f"{n} is NOT prime")

isprime(input("Enter a number: "))