#copying a list:
my_foods= ['pizza','falafel','carrot cake']
friend_foods= my_foods [:]

print('My favorite foods are:')
print(my_foods)

print("\n My friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("my favorite foods are:")
print(my_foods)
print("my friend's favorite foods are:")
print(friend_foods)

my_foods=friend_foods
friend_foods=my_foods
print(my_foods)
print(friend_foods)

# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:

my_cars= ['honda','toyota','subaru','audi', 'bmw', 'ford','nisssan']
print("The first three items in the list are:")
print(my_cars[0:3])

print("Three items from the middle of the list are:")
print(my_cars[3:6])
print("The last three items in the list are:")
print(my_cars[-3:])

#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
#(page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
#Then, do the following:

my_pizza = ['cheese','pepperoni','veggie','supreme']
friends_pizza= ['cheese','veggie','pineapple']
my_pizza.append('jalapeno beef')
friends_pizza.append('margarita')
print("my favorite type of pizzas are:")
print(my_pizza)
print("my friend's favorite types of pizza are:")
print(friends_pizza)

print("My favorite pizzas are:")
for pizza in my_pizza:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friends_pizza:
    print(pizza)

#4-12. More Loops: All versions of foods.py in this section have avoided using
#for loops when printing to save space. Choose a version of foods.py, and
#write two for loops to print each list of foods.

print("my favorite foods are:")
for food in my_foods:
    print(food)
print("My friends's favorite foods are:")
for food in friend_foods:
    print(food)