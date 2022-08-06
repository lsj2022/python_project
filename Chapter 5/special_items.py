requested_toppings= ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:

    if requested_topping == "green peppers":
        print( "sorry, we are out of green peppers right now.")
    else:
        print(f"adding {requested_topping}.")
print("\nFinished making your pizza!")

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\n Finished making your pizza")
else:
    print("are you sure you want a plain pizza?")


# using multiple lists:

available_toppings = ['mushrooms','olives','green peppers',
                      'pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms', 'fresh fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"adding {requested_topping}.")
else:
    print(f"sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")