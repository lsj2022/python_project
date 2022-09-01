# 7-1. Rental Car: Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as “Let me see if I can find you
# a Subaru.”

car = input("What type of rental car do you want?")
print(f"Let me see if I can find you a {car}.")

# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message saying
# they’ll have to wait for a table. Otherwise, report that their table is ready.

seats = input("\nHow many people are in your dinning group?")
seats = int(seats)
if seats > 8:
    print("Please wait for a table")
else:
    print("Your table is ready")

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

number = input("What is multiple of 10?")
number = int(number)
if number % 10== 0:
    print(f" Number is a multiple of 10")
else:
    print(f"Number is not a multiple of 10")
