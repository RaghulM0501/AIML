lst = [1,2,3,4,5,6,7,8,9,10]

even_numbers = [x for x in lst if x % 2 == 0]
#If we are using only IF condition in list comprehension then it should be placed at the end after the for loop.
print(even_numbers)
# Output: [2, 4, 6, 8, 10]

Label = ["Even" if item % 2 ==0 else "odd" for item in lst]
#If we are using IF-ELSE condition in list comprehension then it should be placed at the beginning before the for loop.
print(Label)
# Output: ['odd', 'Even', 'odd', 'Even', 'odd', '

#Nested loop in list comprehension'
Pairs = [(i,j) for i in range(3) for j in range(3)]
print(Pairs)

#IF number of words >3 then big else small
Words = ["This","is","a","list","comprehension","example"]
SizeLabel = ["big" if len(word) > 3 else "small" for word in Words]
print(SizeLabel)