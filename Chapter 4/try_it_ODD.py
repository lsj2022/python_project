#4-6. Odd Numbers: Use the third argument of the range() function to make a
#list of the odd numbers from 1 to 20. Use a for loop to print each number.

odd_number= [list(range(1,21,2))]
for odds in odd_number:
    print(odds)

#4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
#print the numbers in your list.

multiple =[]
multiples= list(range (3,30))
for value in multiples:
    multiple.append(value*3)
print(multiple)

#4-8. Cubes: A number raised to the third power is called a cube. For example,
#the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
#is, the cube of each integer from 1 through 10), and use a for loop to print out
#the value of each cube.

cubes= []
for value in range(1,11):
    cubes.append(value**3)
print(cubes)

#4-9. Cube Comprehension: Use a list comprehension to generate a list of the
#first 10 cubes.

cubes = [value**3 for value in range (1,11)]
print(cubes)