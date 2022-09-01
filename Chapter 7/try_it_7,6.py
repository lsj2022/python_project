# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.


prompt = "\n Enter pizza topping of choice:"
prompt += "\n Enter 'quit' when done adding topping"

toppings = ""

while toppings != 'quit':
    toppings = input(prompt)
    print(f"adding {toppings} to your pizza.")



ask = "\n What topping do you want to add?"
ask += "\n Enter 'quit' when done adding toppings"

active = True

while active:
    message = input(ask)
    if message == 'quit':
        active = 