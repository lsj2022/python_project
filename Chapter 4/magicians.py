#for loop
magicians= ['alice','david', 'carolina']
for magician in magicians:
    print(magician)
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"i can't wait to see your next trick, {magician.title()}. \n")
print("Thank You, everyone. That was a great show!")

#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
#pizza names in a list, and then use a for loop to print the name of each pizza.
pizzas= ['chesse pizza','pepperoni pizza','veggie pizza','chicken pizza']
for pizza in pizzas:
    print(f'I love {pizza.title()} the most')
    print(f"I can eat it all day")
print('I really love pizza')

#4-2. Animals: Think of at least three different animals that have a common characteristic.
#Store the names of these animals in a list, and then use a for loop to
#print out the name of each animal.
animals= ['cat','lion','tiger','panther']
for animal in animals:
    print (animal)

for animal in animals:
    print(f'{animal.title()} would make a great pet!')
print('All these animals are in the same cat family.')


