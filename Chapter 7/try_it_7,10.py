# 7-10. Dream Vacation: Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world, where
# would you go? Include a block of code that prints the results of the poll.

dream_vacation = {}

answers = True
while answers:
    name = input("What is your name?")
    vacation = input("Where do you want to travel to?")
    dream_vacation[name] = vacation
    repeat = input(f" Do you want to send the survey to another person? (yes/ no)")
    if repeat == 'no':
        answers = False
        print('completed survey')

for name, vacation in dream_vacation.items():
    print(f"{name.title()} wants to travel to {vacation.title()}")