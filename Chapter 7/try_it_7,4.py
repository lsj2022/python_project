# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.


prompt = "\n Enter pizza topping of choice:"
prompt += "\n Enter 'quit' when done adding topping"

toppings = ""


while toppings != 'quit':
    toppings = input(prompt)
    print(f"adding {toppings} to your pizza.")


