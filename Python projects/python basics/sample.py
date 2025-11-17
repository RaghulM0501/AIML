import math
application_name = "AIML project"
print(application_name[0:2])
version = "1.0.0"
'''First_name = input("Enter your first name: ")
Last_name = input("Enter your last name: ")
User_name = input("Enter your user name: ")

if First_name.isalpha() & Last_name.isalpha():
    print("first name is valid")
else:
    print("numeric value found in first name")'''

X = input("Enter first number: ")
y = input("Enter second number: ")
if type(X) == int and type(y) == int:
    print("both are numeric values")
else:
    print("one of the value is not numeric")
    
Operation = input ("What operation to be performed? +, -, *, /: ")
if Operation == "+":
    result = float(X) + float(y)
    print("The addition of two numbers is: ", result)
elif Operation == "-":
    result = float(X) - float(y)
    print("The subtraction of two numbers is: ", result)
elif Operation == "*":
    result = float(X) * float(y)
    print("The multiplication of two numbers is: ", result)
elif Operation == "/":
    if float(y) != 0:
        result = float(X) / float(y)
        print("The division of two numbers is: ", result)
    else:
        print("Error: Division by zero is not allowed.")