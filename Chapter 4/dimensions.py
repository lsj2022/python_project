#Tuples: immutable list -- values that cannot change
#use ( ) instead of []

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#looping through all values in a tuple
for dimension in dimensions:
    print(dimension)

#writing over a tuple-- you can assign a new value to a variable that represents a tuple

dimensions= (200,50)
print("original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\n Modified dimensions")
for dimension in dimensions:
    print(dimension)

#4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
#simple foods, and store them in a tuple.

foods= ('rice','mashed potato','steamed veggies','corn','mac and cheese')
for food in foods:
    print(food)
food.append('chicken')

print("new menu:")
foods = ('rice', 'mashed potato', 'chicken', 'beef', 'corn', 'mac and cheese')
for food in foods:
    print(food)