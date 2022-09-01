# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.

sandwich_orders = ['trukey sandwich','chicken sandwich','ham and chesse sandwich','BLT sandwich', 'pastarami','pastarami','pastarami']
finished_sandwiches = []

print("We are out of Pastarami")
while sandwich_orders:
    while "pastarami" in sandwich_orders:
         sandwich_orders.remove("pastarami")
    orders= sandwich_orders.pop()
    print(f"Your {orders} is ready.")


