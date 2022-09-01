#using continue in a loop: returns to the beginning of the loop based on the result of a conditional test

current_number = 0
while current_number <10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)


#avoiding infinite loops:
# every while loop needs a stop so it doesn't continue forever

x= 1
while x <= 5:
    print(x)
    x += 1

# test every while loop to make sure the loop stops before continuing to the next code