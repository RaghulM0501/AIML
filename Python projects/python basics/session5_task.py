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
        return "Error: Division by zero is not allowed."
loop = True
while loop:
    X = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    Operation = input ("What operation to be performed? +, -, *, /: ")
    if Operation == "+":
        result = add(X, y)
        print("The addition of two numbers is: ", result)
    elif Operation == "-":
        result = subtract(X, y)
        print("The subtraction of two numbers is: ", result)
    elif Operation == "*":
        result = multiply(X, y)
        print("The multiplication of two numbers is: ", result)
    elif Operation == "/":
        result = divide(X, y)
        print("The division of two numbers is: ", result)
    else:
        print("Invalid operation selected.")
    
    Breakpoint = input("Hit Enter to continue or Type Exit to close application: ")
    if Breakpoint == 'Exit':
        loop = False