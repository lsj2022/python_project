# the while loop in action:
# while loops work if a certain condition is true

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


#letting the user choose when to quit

prompt = "\nTell me something I will repeat it back to you:"
prompt += "\n Enter 'quit' to end the program"

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)


# using a flag:

prompt = "\n Tell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program"

active = True
while active:
    message = input (prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
