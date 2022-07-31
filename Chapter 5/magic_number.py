answer= 17
if answer != 42:
    print("that is not the correct answer. Please try again")
age = 40
if age < 21:
    print("True")

if age <= 21:
    print('True')

if age > 21:
    print("true")
if age >= 21:
    print ("true")

#checking multiple conditions: --  might need multiple conditions to be true to take an action

age_0= 15
age_1= 18
if age_0 >21 and age-1 >= 21:
    print ("TRUE")

# checking if a value is in a list:
requested_toppings =['mushrooms','onions','pineapple']
if 'mushrooms' in requested_toppings:
    print("true")
if "pepperoni"  in requested_toppings:
    print('false')


#checking if a value is NOT in the list
banned_users =['andrew', 'carolina','david']
user= 'marie'

if user not in banned_users:
    print(f'{user.title()}, you can post a response if you wish.')

#Boolean Expressions:

game_active = True
can_edit = False


#5-1. Conditional Tests: Write a series of conditional tests. Print a statement
#describing each test and your prediction for the results of each test. Your code
#should look something like this:

car= 'subaru'
print("is car == 'subaru'? I predict True.")
print(car== 'subaru')


fruit = 'cherry'
print("is fruit == 'cherry'? I predict True")
print(fruit=='cherry')

fruit = 'apple'
print("is fruit == 'apple'? I predict True")
print(fruit== "cherry")

animal = 'dog'
print("is animal == 'dog'? I predict False")
print(animal== "cat")

flower= "rose"
print( "is flower == 'rose'? I predict True")
print(flower== 'rose')

color= "pink"
print("Is color == 'pink'? I predict False")
print(color== "blue")

number = '27'
print("is number == '27'? I predict True")
print(number == "27")

number = "20"
print("is number == '20' I predict False")
print(number== "25")

animal= 'cat'
print("is animal == 'cat'? I predict True")
print(animal== 'cat')

