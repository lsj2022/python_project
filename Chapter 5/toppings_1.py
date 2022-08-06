requested_toppings = ['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
    print("adding mushrooms")
if "pepperoni" in requested_toppings:
    print("adding pepperoni")
if "extra cheese" in requested_toppings:
    print("adding extra cheese")
print('\n Finished making your pizza!')


#5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
#variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

alien_color = ['green','yellow', 'red']
if "green" in alien_color:
     print("You got 5 points")
if "pink" in alien_color:
    print("you got 0 points")

#5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
#write an if-else chain.

alien_color= ['green','yellow','red']
if "green" in alien_color:
    print("5 points")
else:
    print("10 points")

if "pink" in alien_color:
    print("5 points")
else:
    print("10 points")


#5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse
#chain.

alien_color: ['green','yellow','red']
alien_color = "green"
if "green" in alien_color:
    points = 5
elif "yellow" in alien_color:
    points= 10
else:
    "red"in alien_color
    points = 15
print(f'You got {points}.')

alien_color = "yellow"
if "green" in alien_color:
    points = 5
elif "yellow" in alien_color:
    points= 10
else:
    "red"in alien_color
    points = 15
print(f'You got {points}.')

alien_color = "red"
if "green" in alien_color:
    points = 5
elif "yellow" in alien_color:
    points= 10
else:
    "red"in alien_color
    points = 15
print(f'You got {points}.')

#5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
#stage of life. Set a value for the variable age, and then:
age= 1

if age < 2:
    print("Still a baby")
elif age >= 2 and age < 4:
    print("toddler")
elif age >= 4 and age < 13:
    print("kid")
elif age >= 13 and age < 20:
    print("teenager")
elif age >= 20 and age < 65:
    print("adult")
else:
    age> 65
    print("elder")

age= 3

if age < 2:
    print("Still a baby")
elif age >= 2 and age < 4:
    print("toddler")
elif age >= 4 and age < 13:
    print("kid")
elif age >= 13 and age < 20:
    print("teenager")
elif age >= 20 and age < 65:
    print("adult")
else:
    age> 65
    print("elder")
age= 10

if age < 2:
    print("Still a baby")
elif age >= 2 and age < 4:
    print("toddler")
elif age >= 4 and age < 13:
    print("kid")
elif age >= 13 and age < 20:
    print("teenager")
elif age >= 20 and age < 65:
    print("adult")
else:
    age> 65
    print("elder")

age= 18

if age < 2:
    print("Still a baby")
elif age >= 2 and age < 4:
    print("toddler")
elif age >= 4 and age < 13:
    print("kid")
elif age >= 13 and age < 20:
    print("teenager")
elif age >= 20 and age < 65:
    print("adult")
else:
    age> 65
    print("elder")

age= 45

if age < 2:
    print("Still a baby")
elif age >= 2 and age < 4:
    print("toddler")
elif age >= 4 and age < 13:
    print("kid")
elif age >= 13 and age < 20:
    print("teenager")
elif age >= 20 and age < 65:
    print("adult")
else:
    age> 65
    print("elder")

age= 85

if age < 2:
    print("Still a baby")
elif age >= 2 and age < 4:
    print("toddler")
elif age >= 4 and age < 13:
    print("kid")
elif age >= 13 and age < 20:
    print("teenager")
elif age >= 20 and age < 65:
    print("adult")
else:
    age> 65
    print("elder")

# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
# independent if statements that check for certain fruits in your list.

favorite_fruits= ['watermelon','grapes','apple','cherries']
favorite_fruits = "watermelon"
if "watermelon" in favorite_fruits:
    print("You really like watermelon!")
elif "grapes" in favorite_fruits:
    print("You really like grapes")
elif "apples" in favorite_fruits:
    print("You really like apples")
elif "cherries" in favorite_fruits:
    print("you really like cherries")
else:
    print("You don't like that fruit")

favorite_fruits = "grapes"
if "watermelon" in favorite_fruits:
    print("You really like watermelon!")
elif "grapes" in favorite_fruits:
    print("You really like grapes")
elif "apples" in favorite_fruits:
    print("You really like apples")
elif "cherries" in favorite_fruits:
    print("you really like cherries")
else:
    print("You don't like that fruit")

favorite_fruits = "apples"
if "watermelon" in favorite_fruits:
    print("You really like watermelon!")
elif "grapes" in favorite_fruits:
    print("You really like grapes")
elif "apples" in favorite_fruits:
    print("You really like apples")
elif "cherries" in favorite_fruits:
    print("you really like cherries")
else:
    print("You don't like that fruit")

favorite_fruits = "cherries"
if "watermelon" in favorite_fruits:
    print("You really like watermelon!")
elif "grapes" in favorite_fruits:
    print("You really like grapes")
elif "apples" in favorite_fruits:
    print("You really like apples")
elif "cherries" in favorite_fruits:
    print("you really like cherries")
else:
    print("You don't like that fruit")

favorite_fruits = "banana"
if "watermelon" in favorite_fruits:
    print("You really like watermelon!")
elif "grapes" in favorite_fruits:
    print("You really like grapes")
elif "apples" in favorite_fruits:
    print("You really like apples")
elif "cherries" in favorite_fruits:
    print("you really like cherries")
else:
    print("You don't like that fruit")