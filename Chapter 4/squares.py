squares= []
for value in range (1,11):
    square= value**2
    squares.append(square)
print(squares)

squares=[]
for value in range(1,11):
    squares.append(value**2)
print (squares)


#list comprehensions: generates same list in one line of code
squares= [value**2 for value in range(1,11)]
print(squares)

even_numbers= [value *3 for value in range (2,10)]
print(even_numbers)

