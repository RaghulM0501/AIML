a = 4
b = 3
a==b
# True because the values are equal
a is b
# True because both a and b point to the same object in memory
print(id(a),id(b)) # prints the memory addresses of a and b, which are the same

str = ''.join(['p','y','t','h','o','n'])
str1 = 'python'
print(str == str1) # True because the values are equal
print(str is str1) # False because both str and str1 point to the same object in memory
