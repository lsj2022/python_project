#5-2. More Conditional Tests: You don’t have to limit the number of tests you
#create to ten. If you want to try more comparisons, write more tests and add
#them to conditional_tests.py. Have at least one True and one False result for
#each of the following:

# 1. Test for equality and inequality with strings
car= "bmw"
print("My favorite car is: bmw")
print(car== 'bmw')

cars = 'audi'
cars != 'bmw'
print("my favorite car is 'audi'")
print(cars != 'bmw')

# 2. Tests using the .lower() method

animal = "DOG"
print("my favorite animal is a 'dog'")
print(animal.lower() == 'dog')
print(animal =='dog')

# 3. numerical tests involving equality and inequality, greater than and less than, greater than or equal to and less than or equal to

age= 16
print("I am 16 years old")
print(age==16)

age= 20
if age != 22:
    print("I am not 22 years old")
    print( age != 22)

age = 41
if age > 40:
    print( "I am older than 40")
    print(age == 41)

age = 25
if age < 50:
    print(" I am younger than 50")
    print( age == 25)

temperature = 65
if temperature <= 65:
    print( "The weather is cold outside")
    print( temperature==65)

temperature = 85
if temperature >= 80:
    print("It is very hot outside")
    print( temperature)


# 4. tests using the keyword AND the OR keyword

answer_0= 20
answer_1 = 25
if answer_0 and answer_1 < 26:
    print(" You are correct!")




#5. Test wether an item is in a list

# 6. Test wether an iteam is not in a list

