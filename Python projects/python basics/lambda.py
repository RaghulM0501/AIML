# Anonymous function to find even numbers
#syntax: lambda arguments: expression
square = lambda x: x * x # Function to calculate square of a number
print(square(5))  # Output: 25

#example 2: Lambda function with multiple arguments
add = lambda a, b: a + b
print(add(3, 7))  # Output: 10

#This method is used to filter the even numbers from a list
#This method is also used to sort the list based on custom logic


#MAP: applies the function to all the items in the list
#example 3: Using lambda with map
names = ['Alice', 'Bob', 'Charlie', 'David']
#Convert all names to uppercase using map and lambda    
upper_names = list(map(lambda name: name.upper(), names))
print(upper_names)  # Output: ['ALICE', 'BOB', 'CHARLIE', 'DAVID']

